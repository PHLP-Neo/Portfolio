from __future__ import annotations

from contextlib import asynccontextmanager
from dataclasses import dataclass
from typing import Any
import asyncio
import base64
import binascii
import os
import time

# Limit native libraries before importing torch/cv2 where possible.
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")
os.environ.setdefault("OPENCV_NUM_THREADS", "1")

import cv2
import numpy as np
import torch
from fastapi import FastAPI, HTTPException
from fastapi.concurrency import run_in_threadpool
from fastapi.responses import ORJSONResponse
from pydantic import BaseModel, Field
from ultralytics import YOLO

# Runtime knobs. For the main benchmark, start with:
# BATCH_MAX_SIZE=1 BATCH_TIMEOUT_MS=0 INFER_IMGSZ=160 MAX_IMAGE_SIDE=256
MODEL_PATH = os.getenv("MODEL_PATH", "model.pt")
CONF_THRESHOLD = float(os.getenv("CONF_THRESHOLD", "0.25"))
INFER_IMGSZ = int(os.getenv("INFER_IMGSZ", "160"))
MAX_IMAGE_SIDE = int(os.getenv("MAX_IMAGE_SIDE", "256"))
JPEG_QUALITY = int(os.getenv("JPEG_QUALITY", "80"))
BATCH_MAX_SIZE = max(1, int(os.getenv("BATCH_MAX_SIZE", "1")))
BATCH_TIMEOUT_MS = max(0, int(os.getenv("BATCH_TIMEOUT_MS", "0")))
ANNOTATE_INFLIGHT = max(1, int(os.getenv("ANNOTATE_INFLIGHT", "1")))
MAX_DECODED_BYTES = int(os.getenv("MAX_DECODED_BYTES", str(6 * 1024 * 1024)))
QUEUE_MAX_SIZE = int(os.getenv("QUEUE_MAX_SIZE", "64"))

# In a 1-vCPU Kubernetes pod, oversubscription often destroys latency.
torch.set_num_threads(1)
torch.set_num_interop_threads(1)
cv2.setNumThreads(1)

model: YOLO | None = None
request_queue: asyncio.Queue[InferenceJob] | None = None
batch_worker_task: asyncio.Task | None = None
annotate_semaphore: asyncio.Semaphore | None = None


class PredictRequest(BaseModel):
    uuid: str = Field(..., min_length=1)
    image: str = Field(..., min_length=1)


@dataclass(slots=True)
class InferenceJob:
    image: np.ndarray
    future: asyncio.Future[Any]


@asynccontextmanager
async def lifespan(app: FastAPI):
    global model, request_queue, batch_worker_task, annotate_semaphore

    model = YOLO(MODEL_PATH)

    # Fuse Conv+BN where supported. This is a small but valid CPU inference optimisation.
    try:
        model.fuse()
    except Exception:
        pass

    request_queue = asyncio.Queue(maxsize=QUEUE_MAX_SIZE)
    annotate_semaphore = asyncio.Semaphore(ANNOTATE_INFLIGHT)

    # Warm up the model so readiness/liveness probes do not pass before weights are usable.
    warmup = np.zeros((INFER_IMGSZ, INFER_IMGSZ, 3), dtype=np.uint8)
    await run_in_threadpool(_predict_batch_sync, [warmup])

    batch_worker_task = asyncio.create_task(batch_worker())
    yield

    if batch_worker_task is not None:
        batch_worker_task.cancel()
        try:
            await batch_worker_task
        except asyncio.CancelledError:
            pass


app = FastAPI(lifespan=lifespan, default_response_class=ORJSONResponse)


def decode_base64_image(image_b64: str) -> np.ndarray:
    try:
        encoded = image_b64.split(",", 1)[1] if "," in image_b64 else image_b64
        img_bytes = base64.b64decode(encoded, validate=True)
        if len(img_bytes) > MAX_DECODED_BYTES:
            raise HTTPException(status_code=413, detail="Image payload too large")

        img_array = np.frombuffer(img_bytes, dtype=np.uint8)
        image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        if image is None:
            raise ValueError("Decoded image is empty")
        return image
    except HTTPException:
        raise
    except (binascii.Error, ValueError):
        raise HTTPException(status_code=400, detail="Invalid image encoding or format")


def resize_for_inference(image: np.ndarray, max_side: int = MAX_IMAGE_SIDE) -> np.ndarray:
    h, w = image.shape[:2]
    longest = max(h, w)
    if longest <= max_side:
        return image

    scale = max_side / longest
    new_w = max(1, int(round(w * scale)))
    new_h = max(1, int(round(h * scale)))
    return cv2.resize(image, (new_w, new_h), interpolation=cv2.INTER_AREA)


def _predict_batch_sync(images: list[np.ndarray]) -> list[Any]:
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")

    with torch.inference_mode():
        return model.predict(
            source=images,
            conf=CONF_THRESHOLD,
            imgsz=INFER_IMGSZ,
            verbose=False,
        )


async def batch_worker() -> None:
    assert request_queue is not None

    while True:
        first_job = await request_queue.get()
        jobs = [first_job]

        if BATCH_MAX_SIZE > 1 and BATCH_TIMEOUT_MS > 0:
            deadline = time.perf_counter() + (BATCH_TIMEOUT_MS / 1000.0)
            while len(jobs) < BATCH_MAX_SIZE:
                remaining = deadline - time.perf_counter()
                if remaining <= 0:
                    break
                try:
                    jobs.append(await asyncio.wait_for(request_queue.get(), timeout=remaining))
                except asyncio.TimeoutError:
                    break

        images = [job.image for job in jobs]
        futures = [job.future for job in jobs]

        try:
            results = await run_in_threadpool(_predict_batch_sync, images)
            for future, result in zip(futures, results):
                if not future.done():
                    future.set_result(result)
        except Exception as exc:
            for future in futures:
                if not future.done():
                    future.set_exception(exc)


async def predict_batched(image: np.ndarray) -> Any:
    if request_queue is None:
        raise HTTPException(status_code=503, detail="Inference queue not ready")

    if request_queue.full():
        raise HTTPException(status_code=503, detail="Inference queue overloaded")

    loop = asyncio.get_running_loop()
    future: asyncio.Future[Any] = loop.create_future()
    await request_queue.put(InferenceJob(image=image, future=future))
    return await future


def build_predict_response(uuid: str, result: Any) -> dict[str, Any]:
    boxes_out: list[dict[str, float]] = []
    detections: list[str] = []

    boxes = result.boxes
    if boxes is not None and len(boxes) > 0:
        xyxy = boxes.xyxy.cpu().numpy()
        cls = boxes.cls.cpu().numpy().astype(int)
        conf = boxes.conf.cpu().numpy()
        names = result.names

        for (x1, y1, x2, y2), class_id, probability in zip(xyxy, cls, conf):
            detections.append(names[int(class_id)])
            boxes_out.append(
                {
                    "x": float(x1),
                    "y": float(y1),
                    "width": float(x2 - x1),
                    "height": float(y2 - y1),
                    "probability": float(probability),
                }
            )

    speed = result.speed or {}
    return {
        "uuid": uuid,
        "count": len(boxes_out),
        "detections": detections,
        "boxes": boxes_out,
        "speed_preprocess_ms": float(speed.get("preprocess", 0.0)),
        "speed_inference_ms": float(speed.get("inference", 0.0)),
        "speed_postprocess_ms": float(speed.get("postprocess", 0.0)),
    }


def encode_annotated_image(result: Any) -> str:
    annotated = result.plot()
    ok, buffer = cv2.imencode(
        ".jpg",
        annotated,
        [int(cv2.IMWRITE_JPEG_QUALITY), JPEG_QUALITY],
    )
    if not ok:
        raise HTTPException(status_code=500, detail="Failed to encode annotated image")
    return base64.b64encode(buffer).decode("utf-8")


@app.get("/health")
async def health() -> dict[str, Any]:
    queued = request_queue.qsize() if request_queue is not None else 0
    return {
        "status": "ok",
        "model_loaded": model is not None,
        "imgsz": INFER_IMGSZ,
        "max_image_side": MAX_IMAGE_SIDE,
        "batch_max_size": BATCH_MAX_SIZE,
        "batch_timeout_ms": BATCH_TIMEOUT_MS,
        "annotate_inflight": ANNOTATE_INFLIGHT,
        "queue_depth": queued,
        "queue_max_size": QUEUE_MAX_SIZE,
    }


@app.post("/api/predict")
async def predict(request: PredictRequest) -> dict[str, Any]:
    image = resize_for_inference(decode_base64_image(request.image))
    result = await predict_batched(image)
    return build_predict_response(request.uuid, result)


@app.post("/api/annotate")
async def annotate(request: PredictRequest) -> dict[str, Any]:
    if annotate_semaphore is None:
        raise HTTPException(status_code=503, detail="Annotation path not ready")

    image = resize_for_inference(decode_base64_image(request.image))
    result = await predict_batched(image)

    async with annotate_semaphore:
        annotated_b64 = await run_in_threadpool(encode_annotated_image, result)

    payload = build_predict_response(request.uuid, result)
    payload["image"] = annotated_b64
    return payload


from contextlib import asynccontextmanager
from typing import Any
import asyncio
import base64
import binascii
import os

import cv2
import numpy as np
from fastapi import FastAPI, HTTPException
from fastapi.concurrency import run_in_threadpool
from pydantic import BaseModel, Field
from ultralytics import YOLO

MODEL_PATH = os.getenv("MODEL_PATH", "model.pt")
CONF_THRESHOLD = float(os.getenv("CONF_THRESHOLD", "0.25"))
INFER_IMGSZ = int(os.getenv("INFER_IMGSZ", "416"))
MAX_IMAGE_SIDE = int(os.getenv("MAX_IMAGE_SIDE", "1280"))
JPEG_QUALITY = int(os.getenv("JPEG_QUALITY", "85"))
MAX_INFLIGHT = int(os.getenv("MAX_INFLIGHT", "2"))

model: YOLO | None = None
inference_semaphore = asyncio.Semaphore(MAX_INFLIGHT)


class PredictRequest(BaseModel):
    uuid: str = Field(..., min_length=1)
    image: str = Field(..., min_length=1)


@asynccontextmanager
async def lifespan(app: FastAPI):
    global model
    model = YOLO(MODEL_PATH)

    warmup = np.zeros((INFER_IMGSZ, INFER_IMGSZ, 3), dtype=np.uint8)
    await run_in_threadpool(_predict_sync, warmup)

    yield


app = FastAPI(lifespan=lifespan)


def decode_base64_image(image_b64: str) -> np.ndarray:
    try:
        encoded = image_b64.split(",", 1)[1] if "," in image_b64 else image_b64
        img_bytes = base64.b64decode(encoded, validate=True)
        img_array = np.frombuffer(img_bytes, dtype=np.uint8)
        image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        if image is None:
            raise ValueError("Decoded image is empty")

        return image
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


def _predict_sync(image: np.ndarray):
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")

    results = model.predict(
        source=image,
        conf=CONF_THRESHOLD,
        imgsz=INFER_IMGSZ,
        verbose=False,
    )
    return results[0]


async def predict_with_limit(image: np.ndarray):
    async with inference_semaphore:
        return await run_in_threadpool(_predict_sync, image)


def build_predict_response(uuid: str, result: Any) -> dict:
    detections = []
    boxes = []

    for box in result.boxes:
        x1, y1, x2, y2 = box.xyxy[0].tolist()
        label = result.names[int(box.cls[0])]
        probability = float(box.conf[0])

        detections.append(label)
        boxes.append({
            "x": float(x1),
            "y": float(y1),
            "width": float(x2 - x1),
            "height": float(y2 - y1),
            "probability": probability,
        })

    return {
        "uuid": uuid,
        "count": len(boxes),
        "detections": detections,
        "boxes": boxes,
        "speed_preprocess_ms": float(result.speed.get("preprocess", 0.0)),
        "speed_inference_ms": float(result.speed.get("inference", 0.0)),
        "speed_postprocess_ms": float(result.speed.get("postprocess", 0.0)),
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

    return base64.b64encode(buffer.tobytes()).decode("utf-8")


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "model_loaded": model is not None,
        "imgsz": INFER_IMGSZ,
        "max_inflight": MAX_INFLIGHT,
    }


@app.post("/api/predict")
async def predict(request: PredictRequest):
    image = decode_base64_image(request.image)
    image = resize_for_inference(image)
    result = await predict_with_limit(image)
    return build_predict_response(request.uuid, result)


@app.post("/api/annotate")
async def annotate(request: PredictRequest):
    image = decode_base64_image(request.image)
    image = resize_for_inference(image)
    result = await predict_with_limit(image)
    annotated_b64 = await run_in_threadpool(encode_annotated_image, result)

    return {
        "uuid": request.uuid,
        "image": annotated_b64,
    }
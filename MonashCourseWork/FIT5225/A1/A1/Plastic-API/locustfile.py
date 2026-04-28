from pathlib import Path
import base64
import random
import uuid

from locust import task
from locust.contrib.fasthttp import FastHttpUser

TEST_DIR = Path(__file__).parent / "test"
IMAGE_EXTS = {".jpg", ".jpeg", ".png"}


def load_payloads():
    payloads = []

    for path in TEST_DIR.iterdir():
        if path.is_file() and path.suffix.lower() in IMAGE_EXTS:
            encoded = base64.b64encode(path.read_bytes()).decode("utf-8")

            for _ in range(20):
                payloads.append({
                    "uuid": str(uuid.uuid4()),
                    "image": encoded,
                    "name": path.name,
                })

    if not payloads:
        raise RuntimeError(f"No images found in {TEST_DIR}")

    return payloads


PAYLOADS = load_payloads()


class PlasticApiUser(FastHttpUser):
    @task
    def predict(self):
        payload = random.choice(PAYLOADS)

        request_payload = {
            "uuid": payload["uuid"],
            "image": payload["image"],
        }

        with self.client.post(
            "/api/predict",
            json=request_payload,
            name="/api/predict",
            catch_response=True,
        ) as response:
            if response.status_code != 200:
                response.failure(f"HTTP {response.status_code}")
                return

            try:
                data = response.json()
            except Exception:
                response.failure("Invalid JSON response")
                return

            if data.get("uuid") != request_payload["uuid"]:
                response.failure("UUID mismatch")
            elif "count" not in data or "boxes" not in data or "detections" not in data:
                response.failure("Missing required response fields")
            else:
                response.success()
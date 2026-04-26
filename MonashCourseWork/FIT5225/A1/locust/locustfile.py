import base64
import os
import uuid
from locust import HttpUser, task, between

IMAGE_PATH = os.getenv("IMAGE_PATH", "image.jpg")
API_PATH = os.getenv("API_PATH", "/api/predict")

with open(IMAGE_PATH, "rb") as f:
    ENCODED_IMAGE = base64.b64encode(f.read()).decode("utf-8")


class PlasticApiUser(HttpUser):
    wait_time = between(0.5, 1.5)

    @task
    def predict(self):
        payload = {
            "uuid": str(uuid.uuid4()),
            "image": ENCODED_IMAGE
        }

        with self.client.post(
            API_PATH,
            json=payload,
            name="/api/predict",
            catch_response=True
        ) as response:
            if response.status_code != 200:
                response.failure(f"HTTP {response.status_code}: {response.text}")
                return

            try:
                data = response.json()
            except Exception as e:
                response.failure(f"Invalid JSON response: {e}")
                return

            if "count" not in data:
                response.failure(f"Missing 'count' in response: {data}")
                return

            response.success()
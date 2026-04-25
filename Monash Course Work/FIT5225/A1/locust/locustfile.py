import base64
import uuid
from locust import HttpUser, task, between

class PlasticApiUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def predict_image(self):
        image_path = "test.jpg" 
        with open(image_path, "rb") as f:
            img_str = base64.b64encode(f.read()).decode('utf-8')
        payload = {
            "uuid": str(uuid.uuid4()), 
            "image": img_str          
        }
        self.client.post("/api/predict", json=payload)
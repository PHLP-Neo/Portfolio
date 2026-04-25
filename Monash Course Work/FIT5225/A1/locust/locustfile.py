from locust import HttpUser, task, between

class PlasticApiUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def predict_plastic(self):
        image_path = "test.jpg" 
        
        with open(image_path, "rb") as image_file:
            files = {'file': (image_path, image_file, 'image/jpeg')}
            self.client.post("/predict", files=files)
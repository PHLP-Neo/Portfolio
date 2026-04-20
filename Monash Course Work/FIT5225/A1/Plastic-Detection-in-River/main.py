from fastapi import FastAPI
from pydantic import BaseModel
import base64
import numpy as np
import cv2
from ultralytics import YOLO

app = FastAPI()

# 1. 
model = YOLO("yolov8m.pt")

# 2.  [cite: 206, 207]
class PredictRequest(BaseModel):
    uuid: str
    image: str  # 

@app.post("/api/predict")
async def predict(request: PredictRequest):
    # 3. 
    header, encoded = request.image.split(",", 1) if "," in request.image else ("", request.image)
    img_bytes = base64.b64decode(encoded)
    nparr = np.frombuffer(img_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.imread_color)

    # 4. 
    results = model.predict(source=img)
    res = results[0]

    # 5. 
    response = {
        "uuid": request.uuid,
        "count": len(res.boxes),
        "detections": [res.names[int(c)] for c in res.boxes.cls],
        "boxes": [], # 
        "speed_preprocess_ms": res.speed['preprocess'],
        "speed_inference_ms": res.speed['inference'],
        "speed_postprocess_ms": res.speed['postprocess']
    }
    
    return response
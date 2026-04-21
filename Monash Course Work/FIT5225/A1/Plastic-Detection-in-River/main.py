from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import base64
import numpy as np
import cv2
from ultralytics import YOLO

app = FastAPI()

# 1. 
model = YOLO("model.pt")

# 2.  [cite: 206, 207]
class PredictRequest(BaseModel):
    uuid: str
    image: str  # 

@app.post("/api/predict")
async def predict(request: PredictRequest):
    try:
        # 1. 
        header, encoded = request.image.split(",", 1) if "," in request.image else ("", request.image)
        img_bytes = base64.b64decode(encoded)
        
        # 2. 
        nparr = np.frombuffer(img_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        if img is None:
            raise ValueError("Not a valid image")

    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid image encoding or format")
    # 4. 
    results = model.predict(source=img)
    res = results[0]

    # 5. 
    response = {
        "uuid": request.uuid,
        "count": len(res.boxes),
        "detections": [res.names[int(c)] for c in res.boxes.cls],
        "boxes": [
            {
                "box": [float(x) for x in b.xyxy[0]], # [x1, y1, x2, y2]
                "confidence": float(b.conf[0]),
                "label": res.names[int(b.cls[0])]
            } for b in res.boxes
        ], # 
        "speed_preprocess_ms": res.speed['preprocess'],
        "speed_inference_ms": res.speed['inference'],
        "speed_postprocess_ms": res.speed['postprocess']
    }
    
    return response
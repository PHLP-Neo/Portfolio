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

def get_inference_result(image_b64: str):
    try:
        header, encoded = image_b64.split(",", 1) if "," in image_b64 else ("", image_b64)
        img_bytes = base64.b64decode(encoded)
        nparr = np.frombuffer(img_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        if img is None:
            raise ValueError()
        
        results = model.predict(source=img, conf=0.25)
        return img, results[0]
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid image encoding or format")

@app.post("/api/predict")
async def predict(request: PredictRequest):

    _, res = get_inference_result(request.image)

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

@app.post("/api/annotate")
async def annotate(request: PredictRequest):

    _, res = get_inference_result(request.image)
    
    annotated_img = res.plot() 
    
    _, buffer = cv2.imencode('.jpg', annotated_img)

    annotated_b64 = base64.b64encode(buffer).decode('utf-8')
    
    return {
        "uuid": request.uuid,
        "image": annotated_b64  # 
    }
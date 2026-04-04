from fastapi import APIRouter

router = APIRouter(prefix="/api/detections", tags=["Detections"])

@router.post("/")
def create_detection(data: dict):
    print("AI'dan gelen veri:", data)
    return {"status": "alındı"}
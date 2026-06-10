from fastapi import FastAPI
from routes import products, inventory, detections

app = FastAPI()

app.include_router(products.router)
app.include_router(inventory.router)
app.include_router(detections.router)

@app.get("/")
def root():
    return {"message": "API çalışıyor"}
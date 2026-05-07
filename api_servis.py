from fastapi import FastAPI, HTTPException
from typing import List, Optional
import uvicorn

app = FastAPI(title="Akıllı Depo Yönetim Sistemi API")

# Örnek Veri Seti (Gerçek uygulamada burası veritabanına bağlanacak)
inventory_db = [
    {"id": 1, "name": "Lojistik Kutusu A", "stock": 45, "location": "Raf-A1"},
    {"id": 2, "name": "Palet B2", "stock": 12, "location": "Raf-B2"},
    {"id": 3, "name": "Elektronik Parça Kolisi", "stock": 88, "location": "Raf-C3"}
]

@app.get("/inventory", response_model=List[dict])
async def get_all_inventory():
    """Tüm envanter listesini JSON formatında döndürür."""
    return inventory_db

@app.get("/inventory/{item_id}")
async def get_item(item_id: int):
    """Belirli bir ürün ID'sine göre detay getirir."""
    item = next((i for i in inventory_db if i["id"] == item_id), None)
    if not item:
        raise HTTPException(status_code=404, detail="Ürün bulunamadı")
    return item

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

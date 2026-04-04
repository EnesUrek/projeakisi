from fastapi import APIRouter

router = APIRouter(prefix="/api/inventory", tags=["Inventory"])

inventory = {}

@router.get("/")
def get_inventory():
    return inventory

@router.put("/{product_id}")
def update_inventory(product_id: str, data: dict):
    inventory[product_id] = data
    return {"message": "Stok güncellendi"}
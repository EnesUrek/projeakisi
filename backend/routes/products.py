from fastapi import APIRouter

router = APIRouter(prefix="/api/products", tags=["Products"])

products = []

@router.get("/")
def get_products():
    return products

@router.post("/")
def add_product(product: dict):
    products.append(product)
    return {"message": "Ürün eklendi", "data": product}
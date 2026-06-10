from models import Product

def create_product(
    db,
    name,
    barcode,
    category
):
    product = Product(
        name=name,
        barcode=barcode,
        category=category
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    return product

def get_products(db):
    return db.query(Product).all()

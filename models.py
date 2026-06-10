from sqlalchemy import Column,Integer,String,ForeignKey
from database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    barcode = Column(String, unique=True)
    category = Column(String)

class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True)
    rack_code = Column(String, unique=True)

class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True)

    product_id = Column(
        Integer,
        ForeignKey("products.id")
    )

    location_id = Column(
        Integer,
        ForeignKey("locations.id")
    )

    quantity = Column(Integer)

class MovementLog(Base):
    __tablename__ = "movement_logs"

    id = Column(Integer, primary_key=True)

    inventory_id = Column(
        Integer,
        ForeignKey("inventory.id")
    )

    action_type = Column(String)

    quantity = Column(Integer)

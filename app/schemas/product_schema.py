<<<<<<< HEAD
from pydantic import BaseModel
from typing import Optional
from app.schemas.category_schema import CategoryOut
=======

from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, event
from sqlalchemy.orm import sessionmaker, declarative_base, relationship, Session
from pydantic import BaseModel
from typing import Optional
from app.schemas.category_schema import CategoryOut
from app.database_creation.database import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    description = Column(String, nullable=True)
    price = Column(Float)
    quantity = Column(Integer)
    category_id = Column(Integer, ForeignKey("categories.id", ondelete="CASCADE"), nullable=False)
    category = relationship("Category", back_populates="products")

>>>>>>> 992b61b3e04ca8ef3e0923fdc968021f4880b3da

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    quantity: int
    category_id: int

<<<<<<< HEAD
class ProductCreate(ProductBase):
    pass
=======
class ProductCreate(ProductBase): pass
>>>>>>> 992b61b3e04ca8ef3e0923fdc968021f4880b3da

class ProductOut(ProductBase):
    id: int
    category: CategoryOut
    class Config:
<<<<<<< HEAD
        orm_mode = True
=======
        orm_mode = True
>>>>>>> 992b61b3e04ca8ef3e0923fdc968021f4880b3da

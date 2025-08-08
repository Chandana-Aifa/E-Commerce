from pydantic import BaseModel
from typing import Optional
from app.schemas.category_schema import CategoryOut

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    quantity: int
    category_id: int

class ProductCreate(ProductBase):
    pass

class ProductOut(ProductBase):
    id: int
    category: CategoryOut
    class Config:
        orm_mode = True
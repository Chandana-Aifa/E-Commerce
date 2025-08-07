# main.py

from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, event
from sqlalchemy.orm import sessionmaker, declarative_base, relationship, Session
from pydantic import BaseModel
from typing import List, Optional

DATABASE_URL = "sqlite:///./quickcart.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

@event.listens_for(engine, "connect")
def _enable_fk(dbapi_conn, _):
    dbapi_conn.execute("PRAGMA foreign_keys = ON")

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

# Models
class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True)
    products = relationship("Product", back_populates="category",
                            cascade="all, delete", passive_deletes=True)

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    description = Column(String, nullable=True)
    price = Column(Float)
    quantity = Column(Integer)
    category_id = Column(Integer, ForeignKey("categories.id", ondelete="CASCADE"), nullable=False)
    category = relationship("Category", back_populates="products")

Base.metadata.create_all(bind=engine)

# Schemas
class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase): pass

class CategoryOut(CategoryBase):
    id: int
    class Config:
        orm_mode = True

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    quantity: int
    category_id: int

class ProductCreate(ProductBase): pass

class ProductOut(ProductBase):
    id: int
    category: CategoryOut
    class Config:
        orm_mode = True

# Dependency
def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

app = FastAPI(title="QuickCart")

# Product Endpoints
@app.get("/products", response_model=List[ProductOut])
def list_products(skip: int = 0, limit: int = 10,
                  search: Optional[str] = Query(None), db: Session = Depends(get_db)):
    q = db.query(Product)
    if search:
        q = q.filter(Product.name.contains(search))
    return q.offset(skip).limit(limit).all()

@app.get("/products/{product_id}", response_model=ProductOut)
def get_product(product_id: int, db: Session = Depends(get_db)):
    p = db.get(Product, product_id)
    if not p:
        raise HTTPException(404, "Product not found")
    return p

@app.post("/products", response_model=ProductOut)
def create_product(p: ProductCreate, db: Session = Depends(get_db)):
    obj = Product(**p.dict())
    db.add(obj); db.commit(); db.refresh(obj)
    return obj

@app.put("/products/{product_id}", response_model=ProductOut)
def update_product(product_id: int, p: ProductCreate, db: Session = Depends(get_db)):
    obj = db.get(Product, product_id)
    if not obj:
        raise HTTPException(404, "Product not found")
    for k, v in p.dict().items():
        setattr(obj, k, v)
    db.commit(); db.refresh(obj)
    return obj

# Category Endpoints
@app.get("/categories", response_model=List[CategoryOut])
def list_categories(db: Session = Depends(get_db)):
    return db.query(Category).all()

@app.post("/categories", response_model=CategoryOut)
def create_category(c: CategoryCreate, db: Session = Depends(get_db)):
    obj = Category(**c.dict())
    db.add(obj); db.commit(); db.refresh(obj)
    return obj

@app.put("/categories/{category_id}", response_model=CategoryOut)
def update_category(category_id: int, c: CategoryCreate, db: Session = Depends(get_db)):
    obj = db.get(Category, category_id)
    if not obj:
        raise HTTPException(404, "Category not found")
    obj.name = c.name
    db.commit(); db.refresh(obj)
    return obj

@app.delete("/categories/{category_id}", response_model=CategoryOut)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    obj = db.get(Category, category_id)
    if not obj:
        raise HTTPException(404, "Category not found")
    db.delete(obj); db.commit()
    return obj

<<<<<<< HEAD
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.schemas.product_schema import ProductCreate, ProductOut
from app.models.models import Product
from app.database_creation.database import get_db

router = APIRouter()

@router.get("/products", response_model=List[ProductOut])
def list_products(skip: int = 0, limit: int = 10, search: Optional[str] = Query(None), db: Session = Depends(get_db)):
=======
from fastapi import FastAPI, Depends, HTTPException, Query,APIRouter
from app.schemas.product_schema import Product,ProductBase,ProductCreate,ProductOut
from typing import Optional,List
from app.database_creation.database import get_db, Session

app =APIRouter()



@app.get("/products", response_model=List[ProductOut])
def list_products(skip: int = 0, limit: int = 10,
                  search: Optional[str] = Query(None), db: Session = Depends(get_db)):
>>>>>>> 992b61b3e04ca8ef3e0923fdc968021f4880b3da
    q = db.query(Product)
    if search:
        q = q.filter(Product.name.contains(search))
    return q.offset(skip).limit(limit).all()

<<<<<<< HEAD
@router.get("/products/{product_id}", response_model=ProductOut)
=======
@app.get("/products/{product_id}", response_model=ProductOut)
>>>>>>> 992b61b3e04ca8ef3e0923fdc968021f4880b3da
def get_product(product_id: int, db: Session = Depends(get_db)):
    p = db.get(Product, product_id)
    if not p:
        raise HTTPException(404, "Product not found")
    return p

<<<<<<< HEAD
@router.post("/products", response_model=ProductOut)
=======
@app.post("/products", response_model=ProductOut)
>>>>>>> 992b61b3e04ca8ef3e0923fdc968021f4880b3da
def create_product(p: ProductCreate, db: Session = Depends(get_db)):
    obj = Product(**p.dict())
    db.add(obj); db.commit(); db.refresh(obj)
    return obj

<<<<<<< HEAD
@router.put("/products/{product_id}", response_model=ProductOut)
=======
@app.put("/products/{product_id}", response_model=ProductOut)
>>>>>>> 992b61b3e04ca8ef3e0923fdc968021f4880b3da
def update_product(product_id: int, p: ProductCreate, db: Session = Depends(get_db)):
    obj = db.get(Product, product_id)
    if not obj:
        raise HTTPException(404, "Product not found")
    for k, v in p.dict().items():
        setattr(obj, k, v)
    db.commit(); db.refresh(obj)
<<<<<<< HEAD
    return obj

@router.delete("/products/{product_id}", response_model=ProductOut)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    obj = db.get(Product, product_id)
    if not obj:
        raise HTTPException(404, "Product not found")
    db.delete(obj); db.commit()
=======
>>>>>>> 992b61b3e04ca8ef3e0923fdc968021f4880b3da
    return obj
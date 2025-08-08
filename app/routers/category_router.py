<<<<<<< HEAD
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.category_schema import CategoryCreate, CategoryOut
from app.models.models import Category
from app.database_creation.database import get_db

router = APIRouter()

@router.get("/categories", response_model=List[CategoryOut])
def list_categories(db: Session = Depends(get_db)):
    return db.query(Category).all()

@router.post("/categories", response_model=CategoryOut)
=======
from fastapi import FastAPI, Depends, HTTPException, Query,APIRouter
from app.schemas.category_schema import Category,CategoryBase,CategoryCreate,CategoryOut
from typing import Optional,List
from app.database_creation.database import Session,get_db

app = APIRouter()

@app.get("/categories", response_model=List[CategoryOut])
def list_categories(db: Session = Depends(get_db)):
    return db.query(Category).all()

@app.post("/categories", response_model=CategoryOut)
>>>>>>> 992b61b3e04ca8ef3e0923fdc968021f4880b3da
def create_category(c: CategoryCreate, db: Session = Depends(get_db)):
    obj = Category(**c.dict())
    db.add(obj); db.commit(); db.refresh(obj)
    return obj

<<<<<<< HEAD
@router.put("/categories/{category_id}", response_model=CategoryOut)
=======
@app.put("/categories/{category_id}", response_model=CategoryOut)
>>>>>>> 992b61b3e04ca8ef3e0923fdc968021f4880b3da
def update_category(category_id: int, c: CategoryCreate, db: Session = Depends(get_db)):
    obj = db.get(Category, category_id)
    if not obj:
        raise HTTPException(404, "Category not found")
    obj.name = c.name
    db.commit(); db.refresh(obj)
    return obj

<<<<<<< HEAD
@router.delete("/categories/{category_id}", response_model=CategoryOut)
=======
@app.delete("/categories/{category_id}", response_model=CategoryOut)
>>>>>>> 992b61b3e04ca8ef3e0923fdc968021f4880b3da
def delete_category(category_id: int, db: Session = Depends(get_db)):
    obj = db.get(Category, category_id)
    if not obj:
        raise HTTPException(404, "Category not found")
    db.delete(obj); db.commit()
<<<<<<< HEAD
    return obj
=======
    return obj
>>>>>>> 992b61b3e04ca8ef3e0923fdc968021f4880b3da

from fastapi import FastAPI, Depends, HTTPException, Query,APIRouter
from app.schemas.category_schema import Category,CategoryBase,CategoryCreate,CategoryOut
from typing import Optional,List
from app.database_creation.database import Session,get_db

app = APIRouter()

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

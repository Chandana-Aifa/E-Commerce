from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, event
from sqlalchemy.orm import sessionmaker, declarative_base, relationship, Session
from pydantic import BaseModel
from app.database_creation.database import Base




class Category(Base):

    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True)
    products = relationship("Product", back_populates="category",
                            cascade="all, delete", passive_deletes=True)
# Schemas
class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase): pass

class CategoryOut(CategoryBase):
    id: int
    class Config:
        orm_mode = True
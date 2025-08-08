from fastapi import FastAPI
from app.database_creation.database import engine, Base
from app.routers import category_router, product_router

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="QuickCart")

# Include routers
app.include_router(category_router.router)
app.include_router(product_router.router)
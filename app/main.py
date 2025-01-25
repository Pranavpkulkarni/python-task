from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models import Base
from app.schemas import ProductCreate, ProductUpdate, ProductOut
from app.crud import get_products, get_product_by_id, create_product, update_product

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/product/list", response_model=list[ProductOut])
def list_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_products(db, skip=skip, limit=limit)

@app.get("/product/{pid}/info", response_model=ProductOut)
def product_info(pid: int, db: Session = Depends(get_db)):
    product = get_product_by_id(db, pid)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/product/add", response_model=ProductOut)
def add_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, product)

@app.put("/product/{pid}/update", response_model=ProductOut)
def update_product_info(pid: int, product: ProductUpdate, db: Session = Depends(get_db)):
    updated_product = update_product(db, pid, product)
    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product

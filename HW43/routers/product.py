from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from core.database import get_db
from schemas.schemas import ProductCreate, ProductUpdate, ProductOut
from services.product_service import ProductService

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/", response_model=List[ProductOut])
def get_products(db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.get_all_products()

@router.get("/{product_id}", response_model=ProductOut)
def get_product(product_id: int, db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.get_product(product_id)

@router.post("/", response_model=ProductOut)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.create_product(product)

@router.put("/{product_id}", response_model=ProductOut)
def update_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.update_product(product_id, product)

@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.delete_product(product_id)
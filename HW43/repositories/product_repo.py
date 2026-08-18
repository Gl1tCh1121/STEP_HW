from sqlalchemy.orm import Session
from models.domain import Product
from schemas.schemas import ProductCreate, ProductUpdate

class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Product).all()

    def get_by_id(self, product_id: int):
        return self.db.query(Product).filter(Product.id == product_id).first()

    def create(self, product_in: ProductCreate):
        new_product = Product(**product_in.model_dump())
        self.db.add(new_product)
        self.db.commit()
        self.db.refresh(new_product)
        return new_product

    def update(self, product_id: int, product_in: ProductUpdate):
        product = self.get_by_id(product_id)
        if product:
            update_data = product_in.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(product, key, value)
            self.db.commit()
            self.db.refresh(product)
        return product

    def delete(self, product_id: int):
        product = self.get_by_id(product_id)
        if product:
            self.db.delete(product)
            self.db.commit()
            return True
        return False
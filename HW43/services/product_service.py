from sqlalchemy.orm import Session
from fastapi import HTTPException
from repositories.product_repo import ProductRepository
from schemas.schemas import ProductCreate, ProductUpdate

class ProductService:
    def __init__(self, db: Session):
        self.repo = ProductRepository(db)

    def get_all_products(self):
        return self.repo.get_all()

    def get_product(self, product_id: int):
        product = self.repo.get_by_id(product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        return product

    def create_product(self, product_in: ProductCreate):
        # აქ შეიძლება დაემატოს ბიზნეს ლოგიკა (მაგ: ფასი ხომ არაა უარყოფითი)
        return self.repo.create(product_in)

    def update_product(self, product_id: int, product_in: ProductUpdate):
        product = self.repo.update(product_id, product_in)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        return product

    def delete_product(self, product_id: int):
        success = self.repo.delete(product_id)
        if not success:
            raise HTTPException(status_code=404, detail="Product not found")
        return {"detail": "Product deleted successfully"}
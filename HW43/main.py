from fastapi import FastAPI
from core.database import engine, Base

# როუტერების იმპორტი (მაგალითად product)
from routers import product

# ბაზის და ცხრილების შექმნა
Base.metadata.create_all(bind=engine)

app = FastAPI(title="E-commerce API")

# როუტერების დარეგისტრირება
app.include_router(product.router)
# აქ ჩაამატებთ დანარჩენ როუტერებს:
# app.include_router(user.router)
# app.include_router(category.router)
# app.include_router(subcategory.router)
# app.include_router(order.router)
# app.include_router(order_item.router)

@app.get("/")
def root():
    return {"message": "Welcome to E-commerce API"}
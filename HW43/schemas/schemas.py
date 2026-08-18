from pydantic import BaseModel, ConfigDict
from typing import Optional

# --- USER SCHEMAS ---
class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None

class UserOut(UserBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

# --- PRODUCT SCHEMAS ---
class ProductBase(BaseModel):
    name: str
    price: float
    subcategory_id: int

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    subcategory_id: Optional[int] = None

class ProductOut(ProductBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

# იგივე ლოგიკით იწერება Category, SubCategory, Order და OrderItem სქემები.
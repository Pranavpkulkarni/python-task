from pydantic import BaseModel, Field
from typing import Optional

class ProductBase(BaseModel):
    name: str
    category: str
    description: Optional[str] = None
    product_image: Optional[str] = None
    sku: str
    unit_of_measure: str
    lead_time: int

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class ProductOut(ProductBase):
    id: int
    created_date: str
    updated_date: str

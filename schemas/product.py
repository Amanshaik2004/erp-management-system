from decimal import Decimal

from pydantic import BaseModel


class ProductCreate(BaseModel):

    product_name: str
    description: str
    price: Decimal
    quantity: int
    category_id: int
    supplier_id: int


class ProductUpdate(BaseModel):

    product_name: str
    description: str
    price: Decimal
    quantity: int
    category_id: int
    supplier_id: int


class ProductResponse(BaseModel):

    id: int
    product_name: str
    description: str
    price: Decimal
    quantity: int
    category_id: int
    supplier_id: int

    class Config:
        from_attributes = True
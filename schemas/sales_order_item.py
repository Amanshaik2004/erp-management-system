from decimal import Decimal

from pydantic import BaseModel


class SalesOrderItemCreate(BaseModel):

    sales_order_id: int
    product_id: int
    quantity: int


class SalesOrderItemResponse(BaseModel):

    id: int
    sales_order_id: int
    product_id: int
    quantity: int
    price: Decimal
    subtotal: Decimal

    class Config:
        from_attributes = True
from decimal import Decimal

from pydantic import BaseModel


class SalesOrderCreate(BaseModel):

    customer_id: int


class SalesOrderUpdate(BaseModel):

    status: str


class SalesOrderResponse(BaseModel):

    id: int
    customer_id: int
    status: str
    total_amount: Decimal

    class Config:
        from_attributes = True
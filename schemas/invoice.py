from decimal import Decimal

from pydantic import BaseModel


class InvoiceCreate(BaseModel):

    sales_order_id: int


class InvoiceResponse(BaseModel):

    id: int
    sales_order_id: int
    invoice_number: str
    total_amount: Decimal
    status: str

    class Config:
        from_attributes = True
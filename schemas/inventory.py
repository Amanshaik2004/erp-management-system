from pydantic import BaseModel


class InventoryCreate(BaseModel):

    product_id: int
    stock_in: int = 0
    stock_out: int = 0


class InventoryResponse(BaseModel):

    id: int
    product_id: int
    stock_in: int
    stock_out: int
    available_stock: int
    transaction_type: str

    class Config:
        from_attributes = True
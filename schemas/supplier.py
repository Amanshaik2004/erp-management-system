from pydantic import BaseModel
from pydantic import EmailStr


class SupplierCreate(BaseModel):

    supplier_name: str
    email: EmailStr
    phone: str
    address: str


class SupplierUpdate(BaseModel):

    supplier_name: str
    email: EmailStr
    phone: str
    address: str


class SupplierResponse(BaseModel):

    id: int
    supplier_name: str
    email: EmailStr
    phone: str
    address: str

    class Config:
        from_attributes = True
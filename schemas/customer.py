from pydantic import BaseModel
from pydantic import EmailStr


class CustomerCreate(BaseModel):

    customer_name: str
    email: EmailStr
    phone: str
    address: str


class CustomerUpdate(BaseModel):

    customer_name: str
    email: EmailStr
    phone: str
    address: str


class CustomerResponse(BaseModel):

    id: int
    customer_name: str
    email: EmailStr
    phone: str
    address: str

    class Config:
        from_attributes = True
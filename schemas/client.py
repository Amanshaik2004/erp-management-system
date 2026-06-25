from pydantic import BaseModel


class ClientCreate(BaseModel):

    client_name: str
    email: str
    phone: str
    company: str
    address: str


class ClientUpdate(BaseModel):

    client_name: str
    email: str
    phone: str
    company: str
    address: str


class ClientResponse(BaseModel):

    id: int
    client_name: str
    email: str
    phone: str
    company: str
    address: str

    class Config:
        from_attributes = True
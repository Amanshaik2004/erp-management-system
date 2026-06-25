from pydantic import BaseModel


class TicketCreate(BaseModel):

    title: str
    description: str
    employee_id: int
    priority: str


class TicketUpdate(BaseModel):

    title: str
    description: str
    priority: str
    status: str
    assigned_to: int | None = None


class TicketResponse(BaseModel):

    id: int
    title: str
    description: str
    employee_id: int
    priority: str
    status: str
    assigned_to: int | None = None

    class Config:
        from_attributes = True
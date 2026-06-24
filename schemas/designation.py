from pydantic import BaseModel


class DesignationCreate(BaseModel):
    designation_name: str
    description: str | None = None
    department_id: int


class DesignationResponse(BaseModel):
    id: int
    designation_name: str
    description: str | None
    department_id: int

    class Config:
        from_attributes = True
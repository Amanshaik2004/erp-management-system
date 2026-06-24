from pydantic import BaseModel


class DepartmentCreate(BaseModel):
    department_name: str
    description: str | None = None


class DepartmentResponse(BaseModel):
    id: int
    department_name: str
    description: str | None

    class Config:
        from_attributes = True
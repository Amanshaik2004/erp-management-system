from datetime import date

from pydantic import BaseModel


class ProjectCreate(BaseModel):

    project_name: str
    description: str
    start_date: date
    end_date: date
    status: str


class ProjectUpdate(BaseModel):

    project_name: str
    description: str
    start_date: date
    end_date: date
    status: str


class ProjectResponse(BaseModel):

    id: int
    project_name: str
    description: str
    start_date: date
    end_date: date
    status: str

    class Config:
        from_attributes = True
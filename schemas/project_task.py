from pydantic import BaseModel


class ProjectTaskCreate(BaseModel):

    project_id: int
    employee_id: int
    task_name: str
    description: str


class ProjectTaskUpdate(BaseModel):

    task_name: str
    description: str
    status: str


class ProjectTaskResponse(BaseModel):

    id: int
    project_id: int
    employee_id: int
    task_name: str
    description: str
    status: str

    class Config:
        from_attributes = True
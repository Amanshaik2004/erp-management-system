from datetime import date
from decimal import Decimal

from pydantic import BaseModel


class TimesheetCreate(BaseModel):

    employee_id: int
    project_task_id: int
    work_date: date
    hours_worked: Decimal
    remarks: str


class TimesheetUpdate(BaseModel):

    work_date: date
    hours_worked: Decimal
    remarks: str


class TimesheetResponse(BaseModel):

    id: int
    employee_id: int
    project_task_id: int
    work_date: date
    hours_worked: Decimal
    remarks: str

    class Config:
        from_attributes = True
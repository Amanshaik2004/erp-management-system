from datetime import date

from pydantic import BaseModel


class LeaveRequestCreate(BaseModel):

    employee_id: int
    leave_type: str
    start_date: date
    end_date: date
    reason: str


class LeaveRequestUpdate(BaseModel):

    leave_type: str
    start_date: date
    end_date: date
    reason: str
    status: str


class LeaveRequestResponse(BaseModel):

    id: int
    employee_id: int
    leave_type: str
    start_date: date
    end_date: date
    reason: str
    status: str

    class Config:
        from_attributes = True
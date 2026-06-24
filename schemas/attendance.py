from datetime import date
from datetime import time

from pydantic import BaseModel


class AttendanceCreate(BaseModel):

    employee_id: int
    attendance_date: date
    check_in: time
    check_out: time
    status: str


class AttendanceUpdate(BaseModel):

    check_in: time
    check_out: time
    status: str


class AttendanceResponse(BaseModel):

    id: int
    employee_id: int
    attendance_date: date
    check_in: time
    check_out: time
    status: str

    class Config:
        from_attributes = True
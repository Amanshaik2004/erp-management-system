from datetime import date
from decimal import Decimal

from pydantic import BaseModel, EmailStr


class EmployeeCreate(BaseModel):
    employee_code: str
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    gender: str
    date_of_birth: date
    hire_date: date
    salary: Decimal
    address: str

    department_id: int
    designation_id: int
    role_id: int


class EmployeeUpdate(BaseModel):
    first_name: str
    last_name: str
    phone: str
    salary: Decimal
    address: str
    department_id: int
    designation_id: int
    role_id: int
    is_active: bool


class EmployeeResponse(BaseModel):
    id: int
    employee_code: str
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    gender: str
    salary: Decimal
    department_id: int
    designation_id: int
    role_id: int
    is_active: bool

    class Config:
        from_attributes = True
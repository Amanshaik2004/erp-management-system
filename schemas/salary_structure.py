from decimal import Decimal
from pydantic import BaseModel


class SalaryStructureCreate(BaseModel):

    employee_id: int
    basic_salary: Decimal
    hra: Decimal
    allowances: Decimal
    bonus: Decimal
    deductions: Decimal


class SalaryStructureUpdate(BaseModel):

    basic_salary: Decimal
    hra: Decimal
    allowances: Decimal
    bonus: Decimal
    deductions: Decimal


class SalaryStructureResponse(BaseModel):

    id: int
    employee_id: int
    basic_salary: Decimal
    hra: Decimal
    allowances: Decimal
    bonus: Decimal
    deductions: Decimal

    class Config:
        from_attributes = True
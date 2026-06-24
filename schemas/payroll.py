from decimal import Decimal

from pydantic import BaseModel


class PayrollCreate(BaseModel):

    employee_id: int
    pay_month: str
    basic_salary: Decimal
    bonus: Decimal
    deduction: Decimal


class PayrollUpdate(BaseModel):

    pay_month: str
    basic_salary: Decimal
    bonus: Decimal
    deduction: Decimal


class PayrollResponse(BaseModel):

    id: int
    employee_id: int
    pay_month: str
    basic_salary: Decimal
    bonus: Decimal
    deduction: Decimal
    net_salary: Decimal

    class Config:
        from_attributes = True
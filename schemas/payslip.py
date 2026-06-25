from decimal import Decimal
from pydantic import BaseModel


class PayslipResponse(BaseModel):

    employee_name: str
    pay_month: str

    basic_salary: Decimal
    hra: Decimal
    allowances: Decimal
    bonus: Decimal
    deductions: Decimal

    net_salary: Decimal

    class Config:
        from_attributes = True
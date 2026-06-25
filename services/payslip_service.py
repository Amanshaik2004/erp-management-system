from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.payroll import Payroll
from models.employee import Employee
from models.salary_structure import SalaryStructure


def get_payslip(
    payroll_id: int,
    db: Session
):

    payroll = (
        db.query(Payroll)
        .filter(Payroll.id == payroll_id)
        .first()
    )

    if not payroll:
        raise HTTPException(
            status_code=404,
            detail="Payroll not found"
        )

    employee = (
        db.query(Employee)
        .filter(Employee.id == payroll.employee_id)
        .first()
    )

    salary = (
        db.query(SalaryStructure)
        .filter(
            SalaryStructure.employee_id == payroll.employee_id
        )
        .first()
    )

    if not salary:
        raise HTTPException(
            status_code=404,
            detail="Salary structure not found"
        )

    return {

        "employee_name":
            f"{employee.first_name} {employee.last_name}",

        "pay_month":
            payroll.pay_month,

        "basic_salary":
            salary.basic_salary,

        "hra":
            salary.hra,

        "allowances":
            salary.allowances,

        "bonus":
            salary.bonus,

        "deductions":
            salary.deductions,

        "net_salary":
            payroll.net_salary

    }
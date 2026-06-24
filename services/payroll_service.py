from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.employee import Employee
from models.payroll import Payroll

from schemas.payroll import PayrollCreate
from schemas.payroll import PayrollUpdate


def create_payroll(payroll: PayrollCreate, db: Session):

    employee = (
        db.query(Employee)
        .filter(Employee.id == payroll.employee_id)
        .first()
    )

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    net_salary = (
        payroll.basic_salary +
        payroll.bonus -
        payroll.deduction
    )

    db_payroll = Payroll(
        employee_id=payroll.employee_id,
        pay_month=payroll.pay_month,
        basic_salary=payroll.basic_salary,
        bonus=payroll.bonus,
        deduction=payroll.deduction,
        net_salary=net_salary
    )

    db.add(db_payroll)
    db.commit()
    db.refresh(db_payroll)

    return db_payroll


def get_all_payroll(db: Session):
    return db.query(Payroll).all()


def get_payroll_by_id(payroll_id: int, db: Session):

    payroll = (
        db.query(Payroll)
        .filter(Payroll.id == payroll_id)
        .first()
    )

    if not payroll:
        raise HTTPException(404, "Payroll not found")

    return payroll


def update_payroll(
    payroll_id: int,
    payroll_data: PayrollUpdate,
    db: Session
):

    payroll = (
        db.query(Payroll)
        .filter(Payroll.id == payroll_id)
        .first()
    )

    if not payroll:
        raise HTTPException(404, "Payroll not found")

    payroll.pay_month = payroll_data.pay_month
    payroll.basic_salary = payroll_data.basic_salary
    payroll.bonus = payroll_data.bonus
    payroll.deduction = payroll_data.deduction
    payroll.net_salary = (
        payroll_data.basic_salary +
        payroll_data.bonus -
        payroll_data.deduction
    )

    db.commit()
    db.refresh(payroll)

    return payroll


def delete_payroll(payroll_id: int, db: Session):

    payroll = (
        db.query(Payroll)
        .filter(Payroll.id == payroll_id)
        .first()
    )

    if not payroll:
        raise HTTPException(404, "Payroll not found")

    db.delete(payroll)
    db.commit()

    return {
        "message": "Payroll deleted successfully"
    }
from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.employee import Employee
from models.salary_structure import SalaryStructure

from schemas.salary_structure import (
    SalaryStructureCreate,
    SalaryStructureUpdate
)


def create_salary_structure(data: SalaryStructureCreate, db: Session):

    employee = db.query(Employee).filter(
        Employee.id == data.employee_id
    ).first()

    if not employee:
        raise HTTPException(404, "Employee not found")

    existing = db.query(SalaryStructure).filter(
        SalaryStructure.employee_id == data.employee_id
    ).first()

    if existing:
        raise HTTPException(400, "Salary structure already exists")

    salary = SalaryStructure(**data.model_dump())

    db.add(salary)
    db.commit()
    db.refresh(salary)

    return salary


def get_all_salary_structures(db: Session):

    return db.query(SalaryStructure).all()


def get_salary_structure_by_id(id: int, db: Session):

    salary = db.query(SalaryStructure).filter(
        SalaryStructure.id == id
    ).first()

    if not salary:
        raise HTTPException(404, "Salary structure not found")

    return salary


def update_salary_structure(
    id: int,
    data: SalaryStructureUpdate,
    db: Session
):

    salary = db.query(SalaryStructure).filter(
        SalaryStructure.id == id
    ).first()

    if not salary:
        raise HTTPException(404, "Salary structure not found")

    for key, value in data.model_dump().items():
        setattr(salary, key, value)

    db.commit()
    db.refresh(salary)

    return salary


def delete_salary_structure(id: int, db: Session):

    salary = db.query(SalaryStructure).filter(
        SalaryStructure.id == id
    ).first()

    if not salary:
        raise HTTPException(404, "Salary structure not found")

    db.delete(salary)
    db.commit()

    return {
        "message": "Salary structure deleted successfully"
    }
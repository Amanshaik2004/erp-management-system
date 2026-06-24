from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.department import Department
from models.designation import Designation
from models.employee import Employee
from models.role import Role

from schemas.employee import EmployeeCreate


def create_employee(employee: EmployeeCreate, db: Session):

    if db.query(Employee).filter(
        Employee.email == employee.email
    ).first():
        raise HTTPException(400, "Email already exists")

    if db.query(Employee).filter(
        Employee.employee_code == employee.employee_code
    ).first():
        raise HTTPException(400, "Employee Code already exists")

    if not db.query(Department).filter(
        Department.id == employee.department_id
    ).first():
        raise HTTPException(404, "Department not found")

    if not db.query(Designation).filter(
        Designation.id == employee.designation_id
    ).first():
        raise HTTPException(404, "Designation not found")

    if not db.query(Role).filter(
        Role.id == employee.role_id
    ).first():
        raise HTTPException(404, "Role not found")

    db_employee = Employee(**employee.model_dump())

    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)

    return db_employee

from fastapi import HTTPException


def get_all_employees(db: Session):
    return db.query(Employee).all()


def get_employee_by_id(employee_id: int, db: Session):
    employee = (
        db.query(Employee)
        .filter(Employee.id == employee_id)
        .first()
    )

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee


def update_employee(employee_id: int, employee_data, db: Session):

    employee = (
        db.query(Employee)
        .filter(Employee.id == employee_id)
        .first()
    )

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    update_data = employee_data.model_dump()

    for key, value in update_data.items():
        setattr(employee, key, value)

    db.commit()
    db.refresh(employee)

    return employee


def delete_employee(employee_id: int, db: Session):

    employee = (
        db.query(Employee)
        .filter(Employee.id == employee_id)
        .first()
    )

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    db.delete(employee)
    db.commit()

    return {
        "message": "Employee deleted successfully"
    }
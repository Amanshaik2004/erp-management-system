from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas.employee import EmployeeCreate, EmployeeResponse
from services.employee_service import create_employee
from schemas.employee import EmployeeUpdate

from services.employee_service import (
    create_employee,
    get_all_employees,
    get_employee_by_id,
    update_employee,
    delete_employee
)

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


@router.post("/", response_model=EmployeeResponse)
def create(
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):
    return create_employee(employee, db)

@router.get("/", response_model=list[EmployeeResponse])
def get_all(
    db: Session = Depends(get_db)
):
    return get_all_employees(db)


@router.get("/{employee_id}", response_model=EmployeeResponse)
def get_one(
    employee_id: int,
    db: Session = Depends(get_db)
):
    return get_employee_by_id(
        employee_id,
        db
    )


@router.put("/{employee_id}", response_model=EmployeeResponse)
def update(
    employee_id: int,
    employee: EmployeeUpdate,
    db: Session = Depends(get_db)
):
    return update_employee(
        employee_id,
        employee,
        db
    )


@router.delete("/{employee_id}")
def delete(
    employee_id: int,
    db: Session = Depends(get_db)
):
    return delete_employee(
        employee_id,
        db
    )
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from schemas.salary_structure import (
    SalaryStructureCreate,
    SalaryStructureUpdate,
    SalaryStructureResponse
)

from services.salary_structure_service import *

router = APIRouter(
    prefix="/salary-structures",
    tags=["Salary Structure"]
)


@router.post("/", response_model=SalaryStructureResponse)
def create(
    salary: SalaryStructureCreate,
    db: Session = Depends(get_db)
):
    return create_salary_structure(salary, db)


@router.get("/", response_model=list[SalaryStructureResponse])
def get_all(
    db: Session = Depends(get_db)
):
    return get_all_salary_structures(db)


@router.get("/{id}", response_model=SalaryStructureResponse)
def get_one(
    id: int,
    db: Session = Depends(get_db)
):
    return get_salary_structure_by_id(id, db)


@router.put("/{id}", response_model=SalaryStructureResponse)
def update(
    id: int,
    salary: SalaryStructureUpdate,
    db: Session = Depends(get_db)
):
    return update_salary_structure(id, salary, db)


@router.delete("/{id}")
def delete(
    id: int,
    db: Session = Depends(get_db)
):
    return delete_salary_structure(id, db)
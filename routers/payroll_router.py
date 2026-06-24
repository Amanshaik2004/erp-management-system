from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from schemas.payroll import (
    PayrollCreate,
    PayrollUpdate,
    PayrollResponse
)

from services.payroll_service import *

router = APIRouter(
    prefix="/payroll",
    tags=["Payroll"]
)


@router.post("/", response_model=PayrollResponse)
def create(
    payroll: PayrollCreate,
    db: Session = Depends(get_db)
):
    return create_payroll(payroll, db)


@router.get("/", response_model=list[PayrollResponse])
def get_all(db: Session = Depends(get_db)):
    return get_all_payroll(db)


@router.get("/{payroll_id}", response_model=PayrollResponse)
def get_one(
    payroll_id: int,
    db: Session = Depends(get_db)
):
    return get_payroll_by_id(payroll_id, db)


@router.put("/{payroll_id}", response_model=PayrollResponse)
def update(
    payroll_id: int,
    payroll: PayrollUpdate,
    db: Session = Depends(get_db)
):
    return update_payroll(
        payroll_id,
        payroll,
        db
    )


@router.delete("/{payroll_id}")
def delete(
    payroll_id: int,
    db: Session = Depends(get_db)
):
    return delete_payroll(
        payroll_id,
        db
    )
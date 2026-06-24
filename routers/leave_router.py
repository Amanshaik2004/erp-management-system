from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from schemas.leave_request import (
    LeaveRequestCreate,
    LeaveRequestUpdate,
    LeaveRequestResponse
)

from services.leave_service import *

router = APIRouter(
    prefix="/leave",
    tags=["Leave Management"]
)


@router.post("/", response_model=LeaveRequestResponse)
def create(
    leave: LeaveRequestCreate,
    db: Session = Depends(get_db)
):
    return create_leave(leave, db)


@router.get("/", response_model=list[LeaveRequestResponse])
def get_all(db: Session = Depends(get_db)):
    return get_all_leave(db)


@router.get("/{leave_id}", response_model=LeaveRequestResponse)
def get_one(
    leave_id: int,
    db: Session = Depends(get_db)
):
    return get_leave_by_id(leave_id, db)


@router.put("/{leave_id}", response_model=LeaveRequestResponse)
def update(
    leave_id: int,
    leave: LeaveRequestUpdate,
    db: Session = Depends(get_db)
):
    return update_leave(
        leave_id,
        leave,
        db
    )


@router.delete("/{leave_id}")
def delete(
    leave_id: int,
    db: Session = Depends(get_db)
):
    return delete_leave(
        leave_id,
        db
    )
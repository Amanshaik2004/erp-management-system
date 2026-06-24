from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from database import get_db

from schemas.attendance import (
    AttendanceCreate,
    AttendanceUpdate,
    AttendanceResponse
)

from services.attendance_service import *

router = APIRouter(
    prefix="/attendance",
    tags=["Attendance"]
)


@router.post("/", response_model=AttendanceResponse)
def create(attendance: AttendanceCreate, db: Session = Depends(get_db)):
    return create_attendance(attendance, db)


@router.get("/", response_model=list[AttendanceResponse])
def get_all(db: Session = Depends(get_db)):
    return get_all_attendance(db)


@router.get("/{attendance_id}", response_model=AttendanceResponse)
def get_one(attendance_id: int, db: Session = Depends(get_db)):
    return get_attendance(attendance_id, db)


@router.put("/{attendance_id}", response_model=AttendanceResponse)
def update(attendance_id: int, attendance: AttendanceUpdate, db: Session = Depends(get_db)):
    return update_attendance(attendance_id, attendance, db)


@router.delete("/{attendance_id}")
def delete(attendance_id: int, db: Session = Depends(get_db)):
    return delete_attendance(attendance_id, db)
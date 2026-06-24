from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.attendance import Attendance
from models.employee import Employee

from schemas.attendance import AttendanceCreate
from schemas.attendance import AttendanceUpdate


def create_attendance(attendance: AttendanceCreate, db: Session):

    employee = (
        db.query(Employee)
        .filter(Employee.id == attendance.employee_id)
        .first()
    )

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    new_attendance = Attendance(
        **attendance.model_dump()
    )

    db.add(new_attendance)
    db.commit()
    db.refresh(new_attendance)

    return new_attendance


def get_all_attendance(db: Session):
    return db.query(Attendance).all()


def get_attendance(attendance_id: int, db: Session):

    attendance = (
        db.query(Attendance)
        .filter(Attendance.id == attendance_id)
        .first()
    )

    if not attendance:
        raise HTTPException(404, "Attendance not found")

    return attendance


def update_attendance(attendance_id: int, attendance_data: AttendanceUpdate, db: Session):

    attendance = (
        db.query(Attendance)
        .filter(Attendance.id == attendance_id)
        .first()
    )

    if not attendance:
        raise HTTPException(404, "Attendance not found")

    for key, value in attendance_data.model_dump().items():
        setattr(attendance, key, value)

    db.commit()
    db.refresh(attendance)

    return attendance


def delete_attendance(attendance_id: int, db: Session):

    attendance = (
        db.query(Attendance)
        .filter(Attendance.id == attendance_id)
        .first()
    )

    if not attendance:
        raise HTTPException(404, "Attendance not found")

    db.delete(attendance)
    db.commit()

    return {"message": "Attendance deleted successfully"}
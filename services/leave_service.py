from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.employee import Employee
from models.leave_request import LeaveRequest
from schemas.leave_request import LeaveRequestCreate, LeaveRequestUpdate


def create_leave(leave: LeaveRequestCreate, db: Session):

    employee = (
        db.query(Employee)
        .filter(Employee.id == leave.employee_id)
        .first()
    )

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    db_leave = LeaveRequest(**leave.model_dump())

    db.add(db_leave)
    db.commit()
    db.refresh(db_leave)

    return db_leave


def get_all_leave(db: Session):
    return db.query(LeaveRequest).all()


def get_leave_by_id(leave_id: int, db: Session):

    leave = (
        db.query(LeaveRequest)
        .filter(LeaveRequest.id == leave_id)
        .first()
    )

    if not leave:
        raise HTTPException(404, "Leave request not found")

    return leave


def update_leave(
    leave_id: int,
    leave_data: LeaveRequestUpdate,
    db: Session
):

    leave = (
        db.query(LeaveRequest)
        .filter(LeaveRequest.id == leave_id)
        .first()
    )

    if not leave:
        raise HTTPException(404, "Leave request not found")

    for key, value in leave_data.model_dump().items():
        setattr(leave, key, value)

    db.commit()
    db.refresh(leave)

    return leave


def delete_leave(
    leave_id: int,
    db: Session
):

    leave = (
        db.query(LeaveRequest)
        .filter(LeaveRequest.id == leave_id)
        .first()
    )

    if not leave:
        raise HTTPException(404, "Leave request not found")

    db.delete(leave)
    db.commit()

    return {
        "message": "Leave request deleted successfully"
    }
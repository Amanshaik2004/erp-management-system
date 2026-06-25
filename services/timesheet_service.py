from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.employee import Employee
from models.project_task import ProjectTask
from models.timesheet import Timesheet

from schemas.timesheet import (
    TimesheetCreate,
    TimesheetUpdate
)


def create_timesheet(data: TimesheetCreate, db: Session):

    employee = db.query(Employee).filter(
        Employee.id == data.employee_id
    ).first()

    if not employee:
        raise HTTPException(404, "Employee not found")

    task = db.query(ProjectTask).filter(
        ProjectTask.id == data.project_task_id
    ).first()

    if not task:
        raise HTTPException(404, "Project task not found")

    timesheet = Timesheet(**data.model_dump())

    db.add(timesheet)
    db.commit()
    db.refresh(timesheet)

    return timesheet


def get_all_timesheets(db: Session):
    return db.query(Timesheet).all()


def get_timesheet_by_id(id: int, db: Session):

    timesheet = db.query(Timesheet).filter(
        Timesheet.id == id
    ).first()

    if not timesheet:
        raise HTTPException(404, "Timesheet not found")

    return timesheet


def update_timesheet(
    id: int,
    data: TimesheetUpdate,
    db: Session
):

    timesheet = db.query(Timesheet).filter(
        Timesheet.id == id
    ).first()

    if not timesheet:
        raise HTTPException(404, "Timesheet not found")

    for key, value in data.model_dump().items():
        setattr(timesheet, key, value)

    db.commit()
    db.refresh(timesheet)

    return timesheet


def delete_timesheet(id: int, db: Session):

    timesheet = db.query(Timesheet).filter(
        Timesheet.id == id
    ).first()

    if not timesheet:
        raise HTTPException(404, "Timesheet not found")

    db.delete(timesheet)
    db.commit()

    return {
        "message": "Timesheet deleted successfully"
    }
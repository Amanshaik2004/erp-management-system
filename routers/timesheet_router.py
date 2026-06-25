from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from schemas.timesheet import (
    TimesheetCreate,
    TimesheetUpdate,
    TimesheetResponse
)

from services.timesheet_service import *

router = APIRouter(
    prefix="/timesheets",
    tags=["Timesheets"]
)


@router.post("/", response_model=TimesheetResponse)
def create(
    timesheet: TimesheetCreate,
    db: Session = Depends(get_db)
):
    return create_timesheet(timesheet, db)


@router.get("/", response_model=list[TimesheetResponse])
def get_all(
    db: Session = Depends(get_db)
):
    return get_all_timesheets(db)


@router.get("/{id}", response_model=TimesheetResponse)
def get_one(
    id: int,
    db: Session = Depends(get_db)
):
    return get_timesheet_by_id(id, db)


@router.put("/{id}", response_model=TimesheetResponse)
def update(
    id: int,
    timesheet: TimesheetUpdate,
    db: Session = Depends(get_db)
):
    return update_timesheet(id, timesheet, db)


@router.delete("/{id}")
def delete(
    id: int,
    db: Session = Depends(get_db)
):
    return delete_timesheet(id, db)
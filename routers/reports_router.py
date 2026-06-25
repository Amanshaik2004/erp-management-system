from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from schemas.employee import EmployeeResponse

from services.report_service import employee_report
from schemas.attendance import AttendanceResponse
from services.report_service import attendance_report
from schemas.leave_request import LeaveRequestResponse
from services.report_service import leave_report
from schemas.inventory import InventoryResponse
from services.report_service import inventory_report

router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


@router.get(
    "/employees",
    response_model=list[EmployeeResponse]
)
def employee_reports(
    db: Session = Depends(get_db)
):

    return employee_report(db)

@router.get(
    "/attendance",
    response_model=list[AttendanceResponse]
)
def attendance_reports(
    db: Session = Depends(get_db)
):

    return attendance_report(db)

@router.get(
    "/leaves",
    response_model=list[LeaveRequestResponse]
)
def leave_reports(
    db: Session = Depends(get_db)
):

    return leave_report(db)

@router.get(
    "/inventory",
    response_model=list[InventoryResponse]
)
def inventory_reports(
    db: Session = Depends(get_db)
):

    return inventory_report(db)
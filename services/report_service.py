from sqlalchemy.orm import Session

from models.employee import Employee
from models.attendance import Attendance
from models.leave_request import LeaveRequest
from models.inventory import Inventory


def employee_report(db: Session):

    return db.query(Employee).all()

def attendance_report(db: Session):

    return db.query(Attendance).all()

def leave_report(db: Session):

    return db.query(LeaveRequest).all()

def inventory_report(db: Session):

    return db.query(Inventory).all()


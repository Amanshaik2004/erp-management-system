from sqlalchemy.orm import Session

from models.employee import Employee
from models.department import Department
from models.attendance import Attendance
from models.leave_request import LeaveRequest
from models.product import Product
from models.ticket import Ticket


def get_dashboard(db: Session):

    return {

        "employees": db.query(Employee).count(),
        "departments": db.query(Department).count(),
        "attendance": db.query(Attendance).count(),
        "leave_requests": db.query(LeaveRequest).count(),
        "products": db.query(Product).count(),
        "tickets": db.query(Ticket).count()

    }
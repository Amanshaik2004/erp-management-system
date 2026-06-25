from fastapi import HTTPException
from sqlalchemy.orm import Session
from utils.search import apply_search
from utils.pagination import paginate
from utils.filter import apply_filter

from models.department import Department
from models.designation import Designation
from models.employee import Employee
from models.role import Role

from schemas.employee import EmployeeCreate
import json

from services.redis_service import redis_client


def create_employee(employee: EmployeeCreate, db: Session):

    if db.query(Employee).filter(
        Employee.email == employee.email
    ).first():
        raise HTTPException(400, "Email already exists")

    if db.query(Employee).filter(
        Employee.employee_code == employee.employee_code
    ).first():
        raise HTTPException(400, "Employee Code already exists")

    if not db.query(Department).filter(
        Department.id == employee.department_id
    ).first():
        raise HTTPException(404, "Department not found")

    if not db.query(Designation).filter(
        Designation.id == employee.designation_id
    ).first():
        raise HTTPException(404, "Designation not found")

    if not db.query(Role).filter(
        Role.id == employee.role_id
    ).first():
        raise HTTPException(404, "Role not found")

    db_employee = Employee(**employee.model_dump())

    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)

    redis_client.delete("employees")

    return db_employee

from fastapi import HTTPException


def get_all_employees(db: Session):
    return db.query(Employee).filter(
    Employee.is_deleted == False).all()


def get_employee_by_id(employee_id: int, db: Session):
    employee = db.query(Employee).filter(
    Employee.id == employee_id,
    Employee.is_deleted == False).first()

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee


def update_employee(employee_id: int, employee_data, db: Session):

    employee = (
        db.query(Employee)
        .filter(Employee.id == employee_id)
        .first()
    )

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    update_data = employee_data.model_dump()

    for key, value in update_data.items():
        setattr(employee, key, value)

    db.commit()
    db.refresh(employee)
    redis_client.delete("employees")

    return employee


def delete_employee(employee_id: int, db: Session):

    employee = (
        db.query(Employee)
        .filter(Employee.id == employee_id)
        .first()
    )

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    employee.is_deleted = True

    db.commit()
    redis_client.delete("employees")

    return {
    
    "message": "Employee deleted successfully"
    
    }



from sqlalchemy import asc, desc

from utils.search import apply_search
from utils.pagination import paginate

def get_all_employees_service(
    db: Session,
    search: str = None,
    page: int = 1,
    size: int = 10,
    department_id: int = None,
    designation_id: int = None
):

    # Cache only when using the default employee list
    if (
        not search
        and page == 1
        and size == 10
        and department_id is None
        and designation_id is None
    ):
        cached = redis_client.get("employees")

        if cached:
            return json.loads(cached)

    query = db.query(Employee).filter(
        Employee.is_deleted == False
    )

    query = apply_search(
        query,
        Employee,
        search,
        [
            "first_name",
            "last_name",
            "email"
        ]
    )

    query = apply_filter(
        query,
        Employee,
        {
            "department_id": department_id,
            "designation_id": designation_id
        }
    )

    query = paginate(
        query,
        page,
        size
    )

    employees = query.all()

    if (
        not search
        and page == 1
        and size == 10
        and department_id is None
        and designation_id is None
    ):
        redis_client.set(
            "employees",
            json.dumps(
                [
                    {
                        "id": employee.id,
                        "first_name": employee.first_name,
                        "last_name": employee.last_name,
                        "email": employee.email
                    }
                    for employee in employees
                ]
            ),
            ex=60
        )

    return employees
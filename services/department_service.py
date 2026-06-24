from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.department import Department
from schemas.department import DepartmentCreate


def create_department(department: DepartmentCreate, db: Session):

    existing = (
        db.query(Department)
        .filter(
            Department.department_name == department.department_name
        )
        .first()
    )

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Department already exists"
        )

    new_department = Department(
        department_name=department.department_name,
        description=department.description
    )

    db.add(new_department)
    db.commit()
    db.refresh(new_department)

    return new_department
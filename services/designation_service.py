from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.department import Department
from models.designation import Designation
from schemas.designation import DesignationCreate


def create_designation(
    designation: DesignationCreate,
    db: Session
):

    department = (
        db.query(Department)
        .filter(
            Department.id == designation.department_id
        )
        .first()
    )

    if not department:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )

    existing = (
        db.query(Designation)
        .filter(
            Designation.designation_name == designation.designation_name
        )
        .first()
    )

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Designation already exists"
        )

    new_designation = Designation(
        designation_name=designation.designation_name,
        description=designation.description,
        department_id=designation.department_id
    )

    db.add(new_designation)
    db.commit()
    db.refresh(new_designation)

    return new_designation
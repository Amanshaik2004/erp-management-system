from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas.department import DepartmentCreate
from schemas.department import DepartmentResponse
from services.department_service import create_department

router = APIRouter(
    prefix="/departments",
    tags=["Departments"]
)


@router.post(
    "/",
    response_model=DepartmentResponse
)
def create(
    department: DepartmentCreate,
    db: Session = Depends(get_db)
):
    return create_department(
        department,
        db
    )
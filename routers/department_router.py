from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.permission_service import require_role

from database import get_db
from schemas.department import DepartmentCreate
from schemas.department import DepartmentResponse
from services.department_service import create_department

router = APIRouter(
    prefix="/departments",
    tags=["Departments"]
)


from fastapi import Depends

@router.post(
    "/",
    response_model=DepartmentResponse
)
def create(
    department: DepartmentCreate,
    db: Session = Depends(get_db),
    current_user = Depends(require_role("ADMIN"))
):
    return create_department(
        department,
        db
    )
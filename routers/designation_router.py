from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas.designation import (
    DesignationCreate,
    DesignationResponse
)
from services.designation_service import create_designation

router = APIRouter(
    prefix="/designations",
    tags=["Designations"]
)


@router.post(
    "/",
    response_model=DesignationResponse
)
def create(
    designation: DesignationCreate,
    db: Session = Depends(get_db)
):
    return create_designation(
        designation,
        db
    )
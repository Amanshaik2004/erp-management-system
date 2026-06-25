from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from database import get_db

from schemas.payslip import PayslipResponse

from services.payslip_service import (
    get_payslip
)

router = APIRouter(
    prefix="/payslips",
    tags=["Payslips"]
)


@router.get(
    "/{payroll_id}",
    response_model=PayslipResponse
)
def generate_payslip(
    payroll_id: int,
    db: Session = Depends(get_db)
):

    return get_payslip(
        payroll_id,
        db
    )
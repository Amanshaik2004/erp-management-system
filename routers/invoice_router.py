from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from database import get_db

from schemas.invoice import (
    InvoiceCreate,
    InvoiceResponse
)

from services.invoice_service import (
    create_invoice,
    get_all_invoices,
    get_invoice_by_id,
    delete_invoice
)

router = APIRouter(
    prefix="/invoices",
    tags=["Invoices"]
)


@router.post(
    "/",
    response_model=InvoiceResponse
)
def create(
    invoice: InvoiceCreate,
    db: Session = Depends(get_db)
):

    return create_invoice(
        invoice,
        db
    )


@router.get(
    "/",
    response_model=list[InvoiceResponse]
)
def get_all(
    db: Session = Depends(get_db)
):

    return get_all_invoices(db)


@router.get(
    "/{invoice_id}",
    response_model=InvoiceResponse
)
def get_one(
    invoice_id: int,
    db: Session = Depends(get_db)
):

    return get_invoice_by_id(
        invoice_id,
        db
    )


@router.delete(
    "/{invoice_id}"
)
def delete(
    invoice_id: int,
    db: Session = Depends(get_db)
):

    return delete_invoice(
        invoice_id,
        db
    )
from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.invoice import Invoice
from models.sales_order import SalesOrder

from schemas.invoice import InvoiceCreate


def create_invoice(
    invoice: InvoiceCreate,
    db: Session
):

    order = (
        db.query(SalesOrder)
        .filter(
            SalesOrder.id == invoice.sales_order_id
        )
        .first()
    )

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Sales order not found"
        )

    existing = (
        db.query(Invoice)
        .filter(
            Invoice.sales_order_id == invoice.sales_order_id
        )
        .first()
    )

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Invoice already exists"
        )

    invoice_count = db.query(Invoice).count()

    invoice_number = (
        f"INV-{invoice_count + 1:06d}"
    )

    db_invoice = Invoice(
        sales_order_id=invoice.sales_order_id,
        invoice_number=invoice_number,
        total_amount=order.total_amount,
        status="UNPAID"
    )

    db.add(db_invoice)

    db.commit()

    db.refresh(db_invoice)

    return db_invoice


def get_all_invoices(db: Session):

    return db.query(Invoice).all()


def get_invoice_by_id(
    invoice_id: int,
    db: Session
):

    invoice = (
        db.query(Invoice)
        .filter(
            Invoice.id == invoice_id
        )
        .first()
    )

    if not invoice:
        raise HTTPException(
            status_code=404,
            detail="Invoice not found"
        )

    return invoice


def delete_invoice(
    invoice_id: int,
    db: Session
):

    invoice = (
        db.query(Invoice)
        .filter(
            Invoice.id == invoice_id
        )
        .first()
    )

    if not invoice:
        raise HTTPException(
            status_code=404,
            detail="Invoice not found"
        )

    db.delete(invoice)

    db.commit()

    return {
        "message": "Invoice deleted successfully"
    }
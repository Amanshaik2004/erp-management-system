from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.supplier import Supplier

from schemas.supplier import (
    SupplierCreate,
    SupplierUpdate
)


def create_supplier(supplier: SupplierCreate, db: Session):

    existing = db.query(Supplier).filter(
        Supplier.email == supplier.email
    ).first()

    if existing:
        raise HTTPException(400, "Supplier already exists")

    db_supplier = Supplier(**supplier.model_dump())

    db.add(db_supplier)
    db.commit()
    db.refresh(db_supplier)

    return db_supplier


def get_all_suppliers(db: Session):
    return db.query(Supplier).all()


def get_supplier_by_id(supplier_id: int, db: Session):

    supplier = db.query(Supplier).filter(
        Supplier.id == supplier_id
    ).first()

    if not supplier:
        raise HTTPException(404, "Supplier not found")

    return supplier


def update_supplier(
    supplier_id: int,
    supplier_data: SupplierUpdate,
    db: Session
):

    supplier = db.query(Supplier).filter(
        Supplier.id == supplier_id
    ).first()

    if not supplier:
        raise HTTPException(404, "Supplier not found")

    for key, value in supplier_data.model_dump().items():
        setattr(supplier, key, value)

    db.commit()
    db.refresh(supplier)

    return supplier


def delete_supplier(
    supplier_id: int,
    db: Session
):

    supplier = db.query(Supplier).filter(
        Supplier.id == supplier_id
    ).first()

    if not supplier:
        raise HTTPException(404, "Supplier not found")

    db.delete(supplier)
    db.commit()

    return {
        "message": "Supplier deleted successfully"
    }
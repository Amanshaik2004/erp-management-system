from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from schemas.supplier import (
    SupplierCreate,
    SupplierUpdate,
    SupplierResponse
)

from services.supplier_service import *

router = APIRouter(
    prefix="/suppliers",
    tags=["Suppliers"]
)


@router.post("/", response_model=SupplierResponse)
def create(
    supplier: SupplierCreate,
    db: Session = Depends(get_db)
):
    return create_supplier(supplier, db)


@router.get("/", response_model=list[SupplierResponse])
def get_all(db: Session = Depends(get_db)):
    return get_all_suppliers(db)


@router.get("/{supplier_id}", response_model=SupplierResponse)
def get_one(
    supplier_id: int,
    db: Session = Depends(get_db)
):
    return get_supplier_by_id(supplier_id, db)


@router.put("/{supplier_id}", response_model=SupplierResponse)
def update(
    supplier_id: int,
    supplier: SupplierUpdate,
    db: Session = Depends(get_db)
):
    return update_supplier(
        supplier_id,
        supplier,
        db
    )


@router.delete("/{supplier_id}")
def delete(
    supplier_id: int,
    db: Session = Depends(get_db)
):
    return delete_supplier(
        supplier_id,
        db
    )
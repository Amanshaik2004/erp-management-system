from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from database import get_db

from schemas.sales_order import (
    SalesOrderCreate,
    SalesOrderUpdate,
    SalesOrderResponse
)

from services.sales_order_service import *

router = APIRouter(
    prefix="/sales-orders",
    tags=["Sales Orders"]
)


@router.post("/", response_model=SalesOrderResponse)
def create(
    order: SalesOrderCreate,
    db: Session = Depends(get_db)
):
    return create_sales_order(order, db)


@router.get("/", response_model=list[SalesOrderResponse])
def get_all(
    db: Session = Depends(get_db)
):
    return get_all_orders(db)


@router.get("/{order_id}", response_model=SalesOrderResponse)
def get_one(
    order_id: int,
    db: Session = Depends(get_db)
):
    return get_order_by_id(order_id, db)


@router.put("/{order_id}", response_model=SalesOrderResponse)
def update(
    order_id: int,
    order: SalesOrderUpdate,
    db: Session = Depends(get_db)
):
    return update_order(order_id, order, db)


@router.delete("/{order_id}")
def delete(
    order_id: int,
    db: Session = Depends(get_db)
):
    return delete_order(order_id, db)
from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.customer import Customer
from models.sales_order import SalesOrder

from schemas.sales_order import (
    SalesOrderCreate,
    SalesOrderUpdate
)


def create_sales_order(
    order: SalesOrderCreate,
    db: Session
):

    customer = (
        db.query(Customer)
        .filter(Customer.id == order.customer_id)
        .first()
    )

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    db_order = SalesOrder(
        customer_id=order.customer_id
    )

    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    return db_order


def get_all_orders(db: Session):

    return db.query(SalesOrder).all()


def get_order_by_id(
    order_id: int,
    db: Session
):

    order = (
        db.query(SalesOrder)
        .filter(SalesOrder.id == order_id)
        .first()
    )

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    return order


def update_order(
    order_id: int,
    order_data: SalesOrderUpdate,
    db: Session
):

    order = (
        db.query(SalesOrder)
        .filter(SalesOrder.id == order_id)
        .first()
    )

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    order.status = order_data.status

    db.commit()
    db.refresh(order)

    return order


def delete_order(
    order_id: int,
    db: Session
):

    order = (
        db.query(SalesOrder)
        .filter(SalesOrder.id == order_id)
        .first()
    )

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    db.delete(order)
    db.commit()

    return {
        "message": "Order deleted successfully"
    }
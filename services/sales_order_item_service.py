from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.product import Product
from models.sales_order import SalesOrder
from models.sales_order_item import SalesOrderItem

from schemas.sales_order_item import SalesOrderItemCreate


def add_item_to_order(
    item: SalesOrderItemCreate,
    db: Session
):

    order = (
        db.query(SalesOrder)
        .filter(SalesOrder.id == item.sales_order_id)
        .first()
    )

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Sales order not found"
        )

    product = (
        db.query(Product)
        .filter(Product.id == item.product_id)
        .first()
    )

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    if product.quantity < item.quantity:
        raise HTTPException(
            status_code=400,
            detail="Insufficient stock"
        )

    subtotal = product.price * item.quantity

    order_item = SalesOrderItem(
        sales_order_id=item.sales_order_id,
        product_id=item.product_id,
        quantity=item.quantity,
        price=product.price,
        subtotal=subtotal
    )

    product.quantity -= item.quantity

    order.total_amount += subtotal

    db.add(order_item)

    db.commit()
    db.refresh(order_item)

    return order_item


def get_order_items(db: Session):

    return db.query(SalesOrderItem).all()
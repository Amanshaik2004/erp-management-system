from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.product import Product
from models.inventory import Inventory

from schemas.inventory import InventoryCreate


def create_inventory(
    inventory: InventoryCreate,
    db: Session
):

    product = (
        db.query(Product)
        .filter(Product.id == inventory.product_id)
        .first()
    )

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    if inventory.stock_in > 0:

        product.quantity += inventory.stock_in

        db_inventory = Inventory(
            product_id=inventory.product_id,
            stock_in=inventory.stock_in,
            stock_out=0,
            available_stock=product.quantity,
            transaction_type="STOCK_IN"
        )

    elif inventory.stock_out > 0:

        if product.quantity < inventory.stock_out:
            raise HTTPException(
                status_code=400,
                detail="Insufficient stock"
            )

        product.quantity -= inventory.stock_out

        db_inventory = Inventory(
            product_id=inventory.product_id,
            stock_in=0,
            stock_out=inventory.stock_out,
            available_stock=product.quantity,
            transaction_type="STOCK_OUT"
        )

    else:
        raise HTTPException(
            status_code=400,
            detail="Provide stock_in or stock_out"
        )

    db.add(db_inventory)
    db.commit()
    db.refresh(db_inventory)

    return db_inventory


def get_inventory(db: Session):

    return db.query(Inventory).all()
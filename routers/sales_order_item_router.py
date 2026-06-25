from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from database import get_db

from schemas.sales_order_item import (
    SalesOrderItemCreate,
    SalesOrderItemResponse
)

from services.sales_order_item_service import (
    add_item_to_order,
    get_order_items
)

router = APIRouter(
    prefix="/sales-order-items",
    tags=["Sales Order Items"]
)


@router.post(
    "/",
    response_model=SalesOrderItemResponse
)
def create(
    item: SalesOrderItemCreate,
    db: Session = Depends(get_db)
):

    return add_item_to_order(
        item,
        db
    )


@router.get(
    "/",
    response_model=list[SalesOrderItemResponse]
)
def get_all(
    db: Session = Depends(get_db)
):

    return get_order_items(db)
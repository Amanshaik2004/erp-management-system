from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from database import get_db

from schemas.inventory import (
    InventoryCreate,
    InventoryResponse
)

from services.inventory_service import (
    create_inventory,
    get_inventory
)

router = APIRouter(
    prefix="/inventory",
    tags=["Inventory"]
)


@router.post(
    "/",
    response_model=InventoryResponse
)
def create(
    inventory: InventoryCreate,
    db: Session = Depends(get_db)
):

    return create_inventory(
        inventory,
        db
    )


@router.get(
    "/",
    response_model=list[InventoryResponse]
)
def get_all(
    db: Session = Depends(get_db)
):

    return get_inventory(db)
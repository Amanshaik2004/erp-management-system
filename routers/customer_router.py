from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from database import get_db

from schemas.customer import (
    CustomerCreate,
    CustomerUpdate,
    CustomerResponse
)

from services.customer_service import (
    create_customer,
    get_all_customers,
    get_customer_by_id,
    update_customer,
    delete_customer
)

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)


@router.post(
    "/",
    response_model=CustomerResponse
)
def create(
    customer: CustomerCreate,
    db: Session = Depends(get_db)
):

    return create_customer(
        customer,
        db
    )


@router.get(
    "/",
    response_model=list[CustomerResponse]
)
def get_all(
    db: Session = Depends(get_db)
):

    return get_all_customers(db)


@router.get(
    "/{customer_id}",
    response_model=CustomerResponse
)
def get_one(
    customer_id: int,
    db: Session = Depends(get_db)
):

    return get_customer_by_id(
        customer_id,
        db
    )


@router.put(
    "/{customer_id}",
    response_model=CustomerResponse
)
def update(
    customer_id: int,
    customer: CustomerUpdate,
    db: Session = Depends(get_db)
):

    return update_customer(
        customer_id,
        customer,
        db
    )


@router.delete(
    "/{customer_id}"
)
def delete(
    customer_id: int,
    db: Session = Depends(get_db)
):

    return delete_customer(
        customer_id,
        db
    )
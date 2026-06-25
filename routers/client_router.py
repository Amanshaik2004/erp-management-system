from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from schemas.client import (
    ClientCreate,
    ClientUpdate,
    ClientResponse
)

from services.client_service import *

router = APIRouter(
    prefix="/clients",
    tags=["Clients"]
)


@router.post("/", response_model=ClientResponse)
def create(
    client: ClientCreate,
    db: Session = Depends(get_db)
):
    return create_client(client, db)


@router.get("/", response_model=list[ClientResponse])
def get_all(
    db: Session = Depends(get_db)
):
    return get_all_clients(db)


@router.get("/{client_id}", response_model=ClientResponse)
def get_one(
    client_id: int,
    db: Session = Depends(get_db)
):
    return get_client_by_id(client_id, db)


@router.put("/{client_id}", response_model=ClientResponse)
def update(
    client_id: int,
    client: ClientUpdate,
    db: Session = Depends(get_db)
):
    return update_client(client_id, client, db)


@router.delete("/{client_id}")
def delete(
    client_id: int,
    db: Session = Depends(get_db)
):
    return delete_client(client_id, db)
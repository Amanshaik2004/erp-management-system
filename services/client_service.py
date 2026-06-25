from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.client import Client
from schemas.client import (
    ClientCreate,
    ClientUpdate
)


def create_client(client: ClientCreate, db: Session):

    existing = db.query(Client).filter(
        Client.email == client.email
    ).first()

    if existing:
        raise HTTPException(400, "Client email already exists")

    db_client = Client(**client.model_dump())

    db.add(db_client)
    db.commit()
    db.refresh(db_client)

    return db_client


def get_all_clients(db: Session):

    return db.query(Client).all()


def get_client_by_id(client_id: int, db: Session):

    client = db.query(Client).filter(
        Client.id == client_id
    ).first()

    if not client:
        raise HTTPException(404, "Client not found")

    return client


def update_client(
    client_id: int,
    client_data: ClientUpdate,
    db: Session
):

    client = db.query(Client).filter(
        Client.id == client_id
    ).first()

    if not client:
        raise HTTPException(404, "Client not found")

    for key, value in client_data.model_dump().items():
        setattr(client, key, value)

    db.commit()
    db.refresh(client)

    return client


def delete_client(client_id: int, db: Session):

    client = db.query(Client).filter(
        Client.id == client_id
    ).first()

    if not client:
        raise HTTPException(404, "Client not found")

    db.delete(client)
    db.commit()

    return {
        "message": "Client deleted successfully"
    }
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from schemas.ticket import (
    TicketCreate,
    TicketUpdate,
    TicketResponse
)

from services.ticket_service import *

router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"]
)


@router.post("/", response_model=TicketResponse)
def create(ticket: TicketCreate, db: Session = Depends(get_db)):
    return create_ticket(ticket, db)


@router.get("/", response_model=list[TicketResponse])
def get_all(db: Session = Depends(get_db)):
    return get_all_tickets(db)


@router.get("/{ticket_id}", response_model=TicketResponse)
def get_one(ticket_id: int, db: Session = Depends(get_db)):
    return get_ticket_by_id(ticket_id, db)


@router.put("/{ticket_id}", response_model=TicketResponse)
def update(ticket_id: int, ticket: TicketUpdate, db: Session = Depends(get_db)):
    return update_ticket(ticket_id, ticket, db)


@router.delete("/{ticket_id}")
def delete(ticket_id: int, db: Session = Depends(get_db)):
    return delete_ticket(ticket_id, db)
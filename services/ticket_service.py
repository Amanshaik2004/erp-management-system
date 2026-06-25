from fastapi import HTTPException
from sqlalchemy.orm import Session
from services.email_service import send_email

from models.employee import Employee
from models.ticket import Ticket

from schemas.ticket import (
    TicketCreate,
    TicketUpdate
)

VALID_STATUS = {

    "OPEN": [
        "ASSIGNED"
    ],

    "ASSIGNED": [
        "IN_PROGRESS"
    ],

    "IN_PROGRESS": [
        "RESOLVED"
    ],

    "RESOLVED": [
        "CLOSED"
    ],

    "CLOSED": []

}


def create_ticket(data: TicketCreate, db: Session):

    employee = db.query(Employee).filter(
        Employee.id == data.employee_id
    ).first()

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    ticket = Ticket(**data.model_dump())

    db.add(ticket)
    db.commit()
    db.refresh(ticket)

    return ticket


def get_all_tickets(db: Session):

    return db.query(Ticket).all()


def get_ticket_by_id(ticket_id: int, db: Session):

    ticket = db.query(Ticket).filter(
        Ticket.id == ticket_id
    ).first()

    if not ticket:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    return ticket


def update_ticket(ticket_id: int, data: TicketUpdate, db: Session):

    ticket = db.query(Ticket).filter(
        Ticket.id == ticket_id
    ).first()

    if not ticket:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    if data.assigned_to is not None:

        assigned_employee = db.query(Employee).filter(
            Employee.id == data.assigned_to
        ).first()

        if not assigned_employee:
            raise HTTPException(
                status_code=404,
                detail="Assigned employee not found"
            )

    current_status = ticket.status
    new_status = data.status

    if new_status != current_status:

        if new_status not in VALID_STATUS[current_status]:

            raise HTTPException(
                status_code=400,
                detail=f"Cannot move from {current_status} to {new_status}"
            )

    for key, value in data.model_dump().items():
        setattr(ticket, key, value)

    db.commit()
    db.refresh(ticket)

    if ticket.assigned_to:
        
        assigned_employee = db.query(Employee).filter(
        Employee.id == ticket.assigned_to).first()

        if assigned_employee:

            send_email(
            to_email=assigned_employee.email,
            subject="Ticket Assigned",
            message=f"You have been assigned Ticket #{ticket.id}."
            )

    return ticket

def delete_ticket(ticket_id: int, db: Session):

    ticket = db.query(Ticket).filter(
        Ticket.id == ticket_id
    ).first()

    if not ticket:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    db.delete(ticket)
    db.commit()

    return {
        "message": "Ticket deleted successfully"
    }
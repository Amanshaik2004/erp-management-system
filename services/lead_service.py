from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.client import Client
from models.lead import Lead

from schemas.lead import (
    LeadCreate,
    LeadUpdate
)

VALID_STATUS = {
    "NEW": ["CONTACTED"],
    "CONTACTED": ["QUALIFIED", "LOST"],
    "QUALIFIED": ["LOST"],
    "LOST": []
}


def create_lead(data: LeadCreate, db: Session):

    client = db.query(Client).filter(
        Client.id == data.client_id
    ).first()

    if not client:
        raise HTTPException(
            status_code=404,
            detail="Client not found"
        )

    lead = Lead(**data.model_dump())

    db.add(lead)
    db.commit()
    db.refresh(lead)

    return lead


def get_all_leads(db: Session):

    return db.query(Lead).all()


def get_lead_by_id(id: int, db: Session):

    lead = db.query(Lead).filter(
        Lead.id == id
    ).first()

    if not lead:
        raise HTTPException(
            status_code=404,
            detail="Lead not found"
        )

    return lead


def update_lead(
    id: int,
    data: LeadUpdate,
    db: Session
):

    lead = db.query(Lead).filter(
        Lead.id == id
    ).first()

    if not lead:
        raise HTTPException(
            status_code=404,
            detail="Lead not found"
        )

    if data.status != lead.status:

        if data.status not in VALID_STATUS[lead.status]:

            raise HTTPException(
                status_code=400,
                detail=f"Cannot move from {lead.status} to {data.status}"
            )

    for key, value in data.model_dump().items():
        setattr(lead, key, value)

    db.commit()
    db.refresh(lead)

    return lead


def delete_lead(id: int, db: Session):

    lead = db.query(Lead).filter(
        Lead.id == id
    ).first()

    if not lead:
        raise HTTPException(
            status_code=404,
            detail="Lead not found"
        )

    db.delete(lead)
    db.commit()

    return {
        "message": "Lead deleted successfully"
    }
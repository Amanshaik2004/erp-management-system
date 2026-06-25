from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.lead import Lead
from models.opportunity import Opportunity

from schemas.opportunity import (
    OpportunityCreate,
    OpportunityUpdate
)

VALID_STAGE = {
    "OPEN": ["NEGOTIATION"],
    "NEGOTIATION": ["WON", "LOST"],
    "WON": [],
    "LOST": []
}


def create_opportunity(data: OpportunityCreate, db: Session):

    lead = db.query(Lead).filter(
        Lead.id == data.lead_id
    ).first()

    if not lead:
        raise HTTPException(
            status_code=404,
            detail="Lead not found"
        )

    opportunity = Opportunity(**data.model_dump())

    db.add(opportunity)

    db.commit()

    db.refresh(opportunity)

    return opportunity


def get_all_opportunities(db: Session):

    return db.query(Opportunity).all()


def get_opportunity_by_id(id: int, db: Session):

    opportunity = db.query(Opportunity).filter(
        Opportunity.id == id
    ).first()

    if not opportunity:
        raise HTTPException(
            status_code=404,
            detail="Opportunity not found"
        )

    return opportunity


def update_opportunity(
    id: int,
    data: OpportunityUpdate,
    db: Session
):

    opportunity = db.query(Opportunity).filter(
        Opportunity.id == id
    ).first()

    if not opportunity:
        raise HTTPException(
            status_code=404,
            detail="Opportunity not found"
        )

    if data.stage != opportunity.stage:

        if data.stage not in VALID_STAGE[opportunity.stage]:

            raise HTTPException(
                status_code=400,
                detail=f"Cannot move from {opportunity.stage} to {data.stage}"
            )

    for key, value in data.model_dump().items():
        setattr(opportunity, key, value)

    db.commit()

    db.refresh(opportunity)

    return opportunity


def delete_opportunity(id: int, db: Session):

    opportunity = db.query(Opportunity).filter(
        Opportunity.id == id
    ).first()

    if not opportunity:
        raise HTTPException(
            status_code=404,
            detail="Opportunity not found"
        )

    db.delete(opportunity)

    db.commit()

    return {
        "message": "Opportunity deleted successfully"
    }
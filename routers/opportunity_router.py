from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from schemas.opportunity import (
    OpportunityCreate,
    OpportunityUpdate,
    OpportunityResponse
)

from services.opportunity_service import *

router = APIRouter(
    prefix="/opportunities",
    tags=["Opportunities"]
)


@router.post("/", response_model=OpportunityResponse)
def create(
    opportunity: OpportunityCreate,
    db: Session = Depends(get_db)
):
    return create_opportunity(opportunity, db)


@router.get("/", response_model=list[OpportunityResponse])
def get_all(
    db: Session = Depends(get_db)
):
    return get_all_opportunities(db)


@router.get("/{id}", response_model=OpportunityResponse)
def get_one(
    id: int,
    db: Session = Depends(get_db)
):
    return get_opportunity_by_id(id, db)


@router.put("/{id}", response_model=OpportunityResponse)
def update(
    id: int,
    opportunity: OpportunityUpdate,
    db: Session = Depends(get_db)
):
    return update_opportunity(id, opportunity, db)


@router.delete("/{id}")
def delete(
    id: int,
    db: Session = Depends(get_db)
):
    return delete_opportunity(id, db)
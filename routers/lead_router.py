from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from schemas.lead import (
    LeadCreate,
    LeadUpdate,
    LeadResponse
)

from services.lead_service import *

router = APIRouter(
    prefix="/leads",
    tags=["Leads"]
)


@router.post("/", response_model=LeadResponse)
def create(
    lead: LeadCreate,
    db: Session = Depends(get_db)
):
    return create_lead(lead, db)


@router.get("/", response_model=list[LeadResponse])
def get_all(
    db: Session = Depends(get_db)
):
    return get_all_leads(db)


@router.get("/{id}", response_model=LeadResponse)
def get_one(
    id: int,
    db: Session = Depends(get_db)
):
    return get_lead_by_id(id, db)


@router.put("/{id}", response_model=LeadResponse)
def update(
    id: int,
    lead: LeadUpdate,
    db: Session = Depends(get_db)
):
    return update_lead(id, lead, db)


@router.delete("/{id}")
def delete(
    id: int,
    db: Session = Depends(get_db)
):
    return delete_lead(id, db)
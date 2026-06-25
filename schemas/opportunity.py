from datetime import date
from decimal import Decimal

from pydantic import BaseModel


class OpportunityCreate(BaseModel):

    lead_id: int
    opportunity_name: str
    amount: Decimal
    expected_close_date: date


class OpportunityUpdate(BaseModel):

    opportunity_name: str
    amount: Decimal
    stage: str
    expected_close_date: date


class OpportunityResponse(BaseModel):

    id: int
    lead_id: int
    opportunity_name: str
    amount: Decimal
    stage: str
    expected_close_date: date

    class Config:
        from_attributes = True
from decimal import Decimal

from pydantic import BaseModel


class LeadCreate(BaseModel):

    client_id: int
    lead_source: str
    expected_value: Decimal
    remarks: str


class LeadUpdate(BaseModel):

    lead_source: str
    status: str
    expected_value: Decimal
    remarks: str


class LeadResponse(BaseModel):

    id: int
    client_id: int
    lead_source: str
    status: str
    expected_value: Decimal
    remarks: str

    class Config:
        from_attributes = True
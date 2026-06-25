from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    DateTime,
    ForeignKey,
    DECIMAL
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class Opportunity(Base):

    __tablename__ = "opportunities"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    lead_id = Column(
        Integer,
        ForeignKey("leads.id"),
        nullable=False
    )

    opportunity_name = Column(
        String(100),
        nullable=False
    )

    amount = Column(
        DECIMAL(12,2),
        nullable=False
    )

    stage = Column(
        String(30),
        nullable=False,
        default="OPEN"
    )

    expected_close_date = Column(
        Date,
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    lead = relationship("Lead")
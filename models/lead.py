from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    DECIMAL
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class Lead(Base):

    __tablename__ = "leads"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    client_id = Column(
        Integer,
        ForeignKey("clients.id"),
        nullable=False
    )

    lead_source = Column(
        String(100),
        nullable=False
    )

    status = Column(
        String(30),
        nullable=False,
        default="NEW"
    )

    expected_value = Column(
        DECIMAL(12,2),
        nullable=False
    )

    remarks = Column(
        String(255)
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    client = relationship("Client")
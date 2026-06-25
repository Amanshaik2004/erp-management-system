from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class Ticket(Base):

    __tablename__ = "tickets"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(
        String(150),
        nullable=False
    )

    description = Column(
        Text,
        nullable=False
    )

    employee_id = Column(
        Integer,
        ForeignKey("employees.id"),
        nullable=False
    )

    assigned_to = Column(
    Integer,
    ForeignKey("employees.id"),
    nullable=True
    )

    priority = Column(
        String(20),
        nullable=False,
        default="MEDIUM"
    )

    status = Column(
        String(30),
        nullable=False,
        default="OPEN"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    employee = relationship(
    "Employee",
    foreign_keys=[employee_id]
    )
    
    assigned_employee = relationship(
    "Employee",
    foreign_keys=[assigned_to]
    
    )
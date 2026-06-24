from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime
)

from sqlalchemy.sql import func

from database import Base


class Customer(Base):

    __tablename__ = "customers"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    customer_name = Column(
        String(100),
        nullable=False
    )

    email = Column(
        String(100),
        unique=True,
        nullable=False
    )

    phone = Column(
        String(15),
        unique=True,
        nullable=False
    )

    address = Column(
        String(255),
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
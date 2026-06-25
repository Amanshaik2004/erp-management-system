from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime
)

from sqlalchemy.sql import func

from database import Base


class Client(Base):

    __tablename__ = "clients"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    client_name = Column(
        String(100),
        nullable=False
    )

    email = Column(
        String(100),
        unique=True,
        nullable=False
    )

    phone = Column(
        String(20),
        nullable=False
    )

    company = Column(
        String(100),
        nullable=False
    )

    address = Column(
        String(255)
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
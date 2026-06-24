from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import text

from sqlalchemy.orm import relationship

from sqlalchemy.sql import func

from database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    username = Column(
        String(50),
        unique=True,
        nullable=False
    )

    email = Column(
        String(100),
        unique=True,
        nullable=False
    )

    password_hash = Column(
    String(255),
    nullable=False
    )

    role_id = Column(
        Integer,
        ForeignKey("roles.id"),
        nullable=False
    )

    is_active = Column(
    Boolean,
    nullable=False,
    server_default=text("1")
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    role = relationship(
        "Role",
        back_populates="users"
    )
from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    DateTime
)

from sqlalchemy.sql import func

from database import Base


class Project(Base):

    __tablename__ = "projects"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    project_name = Column(
        String(100),
        nullable=False
    )

    description = Column(
        String(255)
    )

    start_date = Column(
        Date,
        nullable=False
    )

    end_date = Column(
        Date,
        nullable=False
    )

    status = Column(
        String(30),
        nullable=False,
        default="PLANNING"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
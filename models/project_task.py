from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class ProjectTask(Base):

    __tablename__ = "project_tasks"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    project_id = Column(
        Integer,
        ForeignKey("projects.id"),
        nullable=False
    )

    employee_id = Column(
        Integer,
        ForeignKey("employees.id"),
        nullable=False
    )

    task_name = Column(
        String(100),
        nullable=False
    )

    description = Column(
        String(255)
    )

    status = Column(
        String(30),
        nullable=False,
        default="TODO"
    )

    assigned_date = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    project = relationship("Project")
    employee = relationship("Employee")
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


class Timesheet(Base):

    __tablename__ = "timesheets"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    employee_id = Column(
        Integer,
        ForeignKey("employees.id"),
        nullable=False
    )

    project_task_id = Column(
        Integer,
        ForeignKey("project_tasks.id"),
        nullable=False
    )

    work_date = Column(
        Date,
        nullable=False
    )

    hours_worked = Column(
        DECIMAL(5,2),
        nullable=False
    )

    remarks = Column(
        String(255)
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    employee = relationship("Employee")
    project_task = relationship("ProjectTask")
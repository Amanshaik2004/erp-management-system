from sqlalchemy import (
    Column,
    Integer,
    DECIMAL,
    ForeignKey,
    DateTime
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class SalaryStructure(Base):

    __tablename__ = "salary_structures"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    employee_id = Column(
        Integer,
        ForeignKey("employees.id"),
        nullable=False,
        unique=True
    )

    basic_salary = Column(
        DECIMAL(10, 2),
        nullable=False
    )

    hra = Column(
        DECIMAL(10, 2),
        nullable=False,
        default=0
    )

    allowances = Column(
        DECIMAL(10, 2),
        nullable=False,
        default=0
    )

    bonus = Column(
        DECIMAL(10, 2),
        nullable=False,
        default=0
    )

    deductions = Column(
        DECIMAL(10, 2),
        nullable=False,
        default=0
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    employee = relationship("Employee")
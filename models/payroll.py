from sqlalchemy import (
    Column,
    Integer,
    DECIMAL,
    String,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class Payroll(Base):

    __tablename__ = "payroll"

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

    pay_month = Column(
        String(20),
        nullable=False
    )

    basic_salary = Column(
        DECIMAL(10,2),
        nullable=False
    )

    bonus = Column(
        DECIMAL(10,2),
        nullable=False,
        default=0
    )

    deduction = Column(
        DECIMAL(10,2),
        nullable=False,
        default=0
    )

    net_salary = Column(
        DECIMAL(10,2),
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    employee = relationship("Employee")
from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    DateTime,
    Boolean,
    DECIMAL,
    ForeignKey
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base
from sqlalchemy import Boolean


class Employee(Base):

    __tablename__ = "employees"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    employee_code = Column(
        String(20),
        unique=True,
        nullable=False
    )

    first_name = Column(
        String(50),
        nullable=False
    )

    last_name = Column(
        String(50),
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

    gender = Column(
        String(10),
        nullable=False
    )

    date_of_birth = Column(
        Date,
        nullable=False
    )

    hire_date = Column(
        Date,
        nullable=False
    )

    salary = Column(
        DECIMAL(10, 2),
        nullable=False
    )

    address = Column(
        String(255)
    )

    department_id = Column(
        Integer,
        ForeignKey("departments.id"),
        nullable=False
    )

    designation_id = Column(
        Integer,
        ForeignKey("designations.id"),
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
        server_default="1"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    is_deleted = Column(
    Boolean,
    default=False,
    nullable=False
    )

    department = relationship("Department")

    designation = relationship("Designation")

    role = relationship("Role")
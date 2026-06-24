from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Date
from sqlalchemy import DateTime
from sqlalchemy import Time
from sqlalchemy import String
from sqlalchemy import ForeignKey

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class Attendance(Base):

    __tablename__ = "attendance"

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

    attendance_date = Column(
        Date,
        nullable=False
    )

    check_in = Column(
        Time
    )

    check_out = Column(
        Time
    )

    status = Column(
        String(20),
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    employee = relationship("Employee")
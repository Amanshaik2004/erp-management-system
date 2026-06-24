from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class Designation(Base):

    __tablename__ = "designations"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    designation_name = Column(
        String(100),
        nullable=False,
        unique=True
    )

    description = Column(
        String(255)
    )

    department_id = Column(
        Integer,
        ForeignKey("departments.id"),
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    department = relationship("Department")
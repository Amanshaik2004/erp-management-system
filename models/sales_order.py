from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    DECIMAL
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class SalesOrder(Base):

    __tablename__ = "sales_orders"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    customer_id = Column(
        Integer,
        ForeignKey("customers.id"),
        nullable=False
    )

    order_date = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    status = Column(
        String(30),
        nullable=False,
        default="PENDING"
    )

    total_amount = Column(
        DECIMAL(10,2),
        nullable=False,
        default=0
    )

    customer = relationship("Customer")
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


class Invoice(Base):

    __tablename__ = "invoices"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    sales_order_id = Column(
        Integer,
        ForeignKey("sales_orders.id"),
        nullable=False,
        unique=True
    )

    invoice_number = Column(
        String(50),
        unique=True,
        nullable=False
    )

    invoice_date = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    total_amount = Column(
        DECIMAL(10, 2),
        nullable=False
    )

    status = Column(
        String(20),
        nullable=False,
        default="UNPAID"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    sales_order = relationship("SalesOrder")
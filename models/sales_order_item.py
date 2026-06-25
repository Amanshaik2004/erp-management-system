from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    DECIMAL
)

from sqlalchemy.orm import relationship

from database import Base


class SalesOrderItem(Base):

    __tablename__ = "sales_order_items"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    sales_order_id = Column(
        Integer,
        ForeignKey("sales_orders.id"),
        nullable=False
    )

    product_id = Column(
        Integer,
        ForeignKey("products.id"),
        nullable=False
    )

    quantity = Column(
        Integer,
        nullable=False
    )

    price = Column(
        DECIMAL(10,2),
        nullable=False
    )

    subtotal = Column(
        DECIMAL(10,2),
        nullable=False
    )

    sales_order = relationship("SalesOrder")
    product = relationship("Product")
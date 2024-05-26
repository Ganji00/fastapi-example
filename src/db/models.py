"""
ORM models.
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, declarative_base

Base = declarative_base()


class Customer(Base):
    """
    The customers table.
    """

    __tablename__ = "customer"

    customer_id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = Column(String)
    last_name: Mapped[str] = Column(String)


class Order(Base):
    """
    The orders table.
    """

    __tablename__ = "order"

    order_id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    customer_id: Mapped[int] = Column(Integer, ForeignKey("customer.customer_id"))
    order_description: Mapped[str] = Column(String)
    order_total: Mapped[float] = Column(Integer)

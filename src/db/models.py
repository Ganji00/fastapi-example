"""
ORM models.
"""

from typing import Type

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, declarative_base

Base: Type = declarative_base()


class Customer(Base):
    """
    The customers table.
    """

    __tablename__ = "customer"

    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = Column(String)
    last_name: Mapped[str] = Column(String)


class Order(Base):
    """
    The orders table.
    """

    __tablename__ = "order"

    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    customer_id: Mapped[int] = Column(Integer, ForeignKey("customer.id"))
    description: Mapped[str] = Column(String)
    total: Mapped[float] = Column(Integer)

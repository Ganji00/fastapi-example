"""
ORM models.
"""

from typing import Type

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, declarative_base, mapped_column

Base: Type = declarative_base()


class Customer(Base):
    """
    The customers table.
    """

    __tablename__ = "customer"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String)


class Order(Base):
    """
    The orders table.
    """

    __tablename__ = "order"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    customer_id: Mapped[int] = mapped_column(Integer, ForeignKey("customer.id"))
    description: Mapped[str] = mapped_column(String)
    total: Mapped[float] = mapped_column(Integer)

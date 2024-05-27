"""
Implements order schemas
"""

from pydantic import BaseModel, ConfigDict


class OrderBase(BaseModel):
    """
    Order base schema
    """

    customer_id: int
    description: str
    total: float

    model_config = ConfigDict(from_attributes=True)


class OrderResponse(OrderBase):
    """
    Order response schema
    """

    id: int


class OrderRequest(OrderBase):
    """
    Order request schema
    """

    pass

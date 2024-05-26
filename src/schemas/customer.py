"""
Implements customer schemas
"""

from pydantic import BaseModel, ConfigDict


class CustomerBase(BaseModel):
    """
    Customer base schema
    """

    first_name: str
    last_name: str

    model_config = ConfigDict(from_attributes=True)


class CustomerResponse(CustomerBase):
    """
    Customer response schema
    """

    id: int


class CustomerRequest(CustomerBase):
    """
    Customer request schema
    """

    pass

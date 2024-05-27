from sqlalchemy.ext.asyncio import AsyncSession

from src.db.models import Customer
from tests.utils.utils import random_string


def create_random_customer(db: AsyncSession) -> Customer:
    customer = Customer(
        first_name=random_string(),
        last_name=random_string(),
    )
    db.add(customer)
    db.commit()
    return customer

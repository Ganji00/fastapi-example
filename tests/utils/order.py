import random

from sqlalchemy.ext.asyncio import AsyncSession

from src.db.models import Order
from tests.utils.utils import random_string


async def create_random_order(db: AsyncSession) -> Order:
    customer = Order(
        customer_id=1, description=random_string(), total=random.uniform(1.0, 100.0)
    )
    db.add(customer)
    await db.commit()
    return customer

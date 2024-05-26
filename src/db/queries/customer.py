from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.models import Customer


async def get_customers(db: AsyncSession):
    q = select(Customer)
    result = await db.execute(q)
    customers = result.scalars().all()
    return customers

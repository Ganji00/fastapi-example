from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.database import get_db
from src.db.queries.customer import get_customers
from src.schemas.customer import Customer

router = APIRouter(
    prefix="/customer",
    tags=["customer"],
)


@router.get("/", response_model=List[Customer])
async def read_customers(db: AsyncSession = Depends(get_db)):
    customers = await get_customers(db=db)
    return customers

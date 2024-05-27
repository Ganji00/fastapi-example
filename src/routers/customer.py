from typing import List

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.database import get_db
from src.db.models import Customer, Order
from src.schemas.customer import CustomerRequest, CustomerResponse
from src.schemas.order import OrderResponse

router = APIRouter(
    prefix="/customer",
    tags=["customer"],
)


@router.get("/", response_model=List[CustomerResponse])
async def read_customers(db: AsyncSession = Depends(get_db)):
    q = select(Customer)
    result = await db.execute(q)
    customers = result.scalars().all()
    return customers


@router.get("/{customer_id}", response_model=CustomerResponse)
async def read_customer(customer_id: int, db: AsyncSession = Depends(get_db)):
    q = select(Customer).filter(Customer.id == customer_id)
    result = await db.execute(q)
    customer = result.scalars().first()
    if not customer:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return customer


@router.get("/{customer_id}/orders", response_model=List[OrderResponse])
async def read_customer_orders(customer_id: int, db: AsyncSession = Depends(get_db)):
    q = select(Order).filter(Order.customer_id == customer_id)
    result = await db.execute(q)
    orders = result.scalars().all()
    return orders


@router.delete("/{customer_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_customer(customer_id: int, db: AsyncSession = Depends(get_db)):
    q = select(Customer).filter(Customer.id == customer_id)
    result = await db.execute(q)
    customer = result.scalars().first()
    if not customer:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        await db.delete(customer)
        await db.commit()


@router.post("/", response_model=CustomerResponse, status_code=status.HTTP_201_CREATED)
async def create_customer(
    customer: CustomerRequest, db: AsyncSession = Depends(get_db)
):
    db_customer = Customer(**customer.model_dump())
    db.add(db_customer)
    await db.commit()
    return db_customer


@router.put("/{customer_id}", response_model=CustomerResponse)
async def update_customer(
    customer_id: int, customer: CustomerRequest, db: AsyncSession = Depends(get_db)
):
    q = select(Customer).filter(Customer.id == customer_id)
    result = await db.execute(q)
    db_customer = result.scalars().first()
    if not db_customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found"
        )
    else:
        db_customer.first_name = customer.first_name
        db_customer.last_name = customer.last_name
        await db.commit()
        return db_customer

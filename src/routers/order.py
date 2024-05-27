from typing import List

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.database import get_db
from src.db.models import Order
from src.schemas.order import OrderRequest, OrderResponse

router = APIRouter(
    prefix="/order",
    tags=["order"],
)


@router.get("/", response_model=List[OrderResponse])
async def read_orders(db: AsyncSession = Depends(get_db)):
    q = select(Order)
    result = await db.execute(q)
    orders = result.scalars().all()
    return orders


@router.get("/{order_id}", response_model=OrderResponse)
async def read_order(order_id: int, db: AsyncSession = Depends(get_db)):
    q = select(Order).filter(Order.id == order_id)
    result = await db.execute(q)
    order = result.scalars().first()
    if not order:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return order


@router.delete("/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_order(order_id: int, db: AsyncSession = Depends(get_db)):
    q = select(Order).filter(Order.id == order_id)
    result = await db.execute(q)
    order = result.scalars().first()
    if not order:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        await db.delete(order)
        await db.commit()


@router.post("/", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
async def create_order(order: OrderRequest, db: AsyncSession = Depends(get_db)):
    db_order = Order(**order.model_dump())
    db.add(db_order)
    await db.commit()
    return db_order


@router.put("/{order_id}", response_model=OrderResponse)
async def update_order(
    order_id: int, order: OrderRequest, db: AsyncSession = Depends(get_db)
):
    q = select(Order).filter(Order.id == order_id)
    result = await db.execute(q)
    db_order = result.scalars().first()
    if not db_order:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Order not found"
        )
    else:
        db_order.description = order.description
        db_order.total = order.total
        db_order.customer_id = order.customer_id
        await db.commit()
        return db_order

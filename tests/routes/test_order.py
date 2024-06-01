import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession

from tests.utils.customer import create_random_customer
from tests.utils.order import create_random_order


@pytest.mark.asyncio
async def test_read_customers(client: TestClient) -> None:
    response = client.get("/order")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_add_order(client: TestClient, db: AsyncSession) -> None:
    await create_random_customer(db)
    response = client.post(
        "/order",
        json={
            "customer_id": 1,
            "description": "test",
            "total": 123.1,
        },
    )
    assert response.status_code == 201


@pytest.mark.asyncio
async def test_update_order(client: TestClient, db: AsyncSession) -> None:
    # we need to create a customer first as order contains foreign key to customer.
    await create_random_customer(db)
    await create_random_order(db)
    response = client.put(
        "/order/1",
        json={
            "customer_id": 1,
            "description": "Changed",
            "total": 200.0,
        },
    )
    assert response.status_code == 200
    assert response.json()["description"] == "Changed"
    assert response.json()["total"] == 200.0


@pytest.mark.asyncio
async def test_read_single_order(client: TestClient, db: AsyncSession) -> None:
    await create_random_customer(db)
    await create_random_order(db)
    response = client.get("/order/1")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_read_single_order_not_found(client: TestClient) -> None:
    response = client.get("/order/999")
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_delete_order(client: TestClient, db: AsyncSession) -> None:
    await create_random_customer(db)
    await create_random_order(db)
    response = client.delete("/order/1")
    assert response.status_code == 204

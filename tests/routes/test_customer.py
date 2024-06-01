import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.database import init_models
from tests.utils.customer import create_random_customer


@pytest.mark.asyncio
async def test_read_customers(client: TestClient) -> None:
    await init_models()
    response = client.get("/customer")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_add_customer(client: TestClient) -> None:
    await init_models()
    response = client.post(
        "/customer",
        json={
            "first_name": "John",
            "last_name": "Doe",
        },
    )
    assert response.status_code == 201


@pytest.mark.asyncio
async def test_update_customer(client: TestClient, db: AsyncSession) -> None:
    await create_random_customer(db)
    response = client.put(
        "/customer/1",
        json={
            "first_name": "John",
            "last_name": "Kiersnowski",
        },
    )
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_read_single_customer(client: TestClient, db: AsyncSession) -> None:
    await create_random_customer(db)
    response = client.get("/customer/1")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_read_single_customer_not_found(client: TestClient) -> None:
    response = client.get("/customer/999")
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_delete_customer(client: TestClient) -> None:
    response = client.delete("/customer/1")
    assert response.status_code == 204

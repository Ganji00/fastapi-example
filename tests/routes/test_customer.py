from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession

from tests.utils.customer import create_random_customer


def test_read_customers(client: TestClient) -> None:
    response = client.get("/customer")
    assert response.status_code == 200


# def test_read_single_customer(client: TestClient, db: AsyncSession) -> None:
#     create_random_customer(db)
#     response = client.get("/customer/1")
#     assert response.status_code == 200

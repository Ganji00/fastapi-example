import pytest
from fastapi.testclient import TestClient

from src.db.database import create_database_engine, create_sessionmaker
from src.main import app


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as client:
        yield client


@pytest.fixture(scope="function")
async def db():
    engine = await create_database_engine()
    session_maker = await create_sessionmaker(engine)
    async with session_maker() as session:
        yield session
    await session.rollback()
    await session.close()
    await engine.dispose(close=True)

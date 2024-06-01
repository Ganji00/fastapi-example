import pytest
import pytest_asyncio
from fastapi.testclient import TestClient

from src.db.database import create_database_engine, create_sessionmaker, init_models
from src.main import app


@pytest.fixture(scope="module")
def client():
    # TODO: run it asynchronously.
    with TestClient(app) as client:
        yield client


@pytest_asyncio.fixture(scope="function")
async def db():
    # TODO: clear the database before each test
    engine = await create_database_engine()
    await init_models()
    session_maker = await create_sessionmaker(engine)
    async with session_maker() as session:
        yield session
    await engine.dispose(close=True)

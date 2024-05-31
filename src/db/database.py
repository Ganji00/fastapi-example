from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from src.core.config import get_application_settings
from src.db.models import Base


async def create_database_engine() -> AsyncEngine:
    """
    Create a new database engine.
    :return: A new database engine.
    """
    settings = get_application_settings()

    sqlalchemy_database_url = (
        f"postgresql+asyncpg://{settings.db_user}:{settings.db_password}@"
        f"{settings.db_host}:{settings.db_port}/{settings.db_name}"
    )

    engine = create_async_engine(sqlalchemy_database_url)
    return engine


async def create_sessionmaker(engine: AsyncEngine) -> async_sessionmaker:
    """
    Create a new sessionmaker.
    :param engine: The database engine.
    """
    return async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def get_db() -> AsyncSession:
    """
    Get a new database session.
    :return: A new database session.
    """
    engine = await create_database_engine()
    sessionmaker = await create_sessionmaker(engine)
    try:
        async with sessionmaker() as session:
            yield session
    finally:
        await session.commit()
        await session.close()
        await engine.dispose(close=True)


async def init_models():
    engine = await create_database_engine()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

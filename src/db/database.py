from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
)

from src.core.config import get_application_settings


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


async def create_sessionmaker(engine: AsyncEngine):
    """
    Create a new sessionmaker.
    :param engine: The database engine.
    """
    return async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

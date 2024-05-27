from typing import Dict

from fastapi import FastAPI

from src.core.config import get_application_settings
from src.routers.customer import router as customer_router
from src.routers.order import router as order_router


def get_app() -> FastAPI:
    """
    Setup FastAPI application and include routers
    :return: FastAPI app.
    """
    settings = get_application_settings()

    # unpack relevant application kwargs
    application = FastAPI(**settings.fastapi_kwargs)

    application.include_router(customer_router)
    application.include_router(order_router)

    return application


app = get_app()


@app.get("/")
async def root() -> Dict[str, str]:
    return {"message": "Hello World"}

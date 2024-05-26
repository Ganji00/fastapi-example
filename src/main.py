from typing import Dict

from fastapi import FastAPI
from src.core.config import get_application_settings


def get_app() -> FastAPI:
    """
    Setup FastAPI application and include routers
    :return: FastAPI app.
    """
    settings = get_application_settings()

    # unpack relevant application kwargs
    application = FastAPI(**settings.fastapi_kwargs)

    return application


app = get_app()


@app.get("/")
async def root() -> Dict[str, str]:
    return {"message": "Hello World"}

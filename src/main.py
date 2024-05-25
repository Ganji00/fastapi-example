from typing import Dict

from fastapi import FastAPI


def get_app() -> FastAPI:
    """
    Setup FastAPI application and include routers
    :return: FastAPI app.
    """
    application = FastAPI()

    return application


app = get_app()


@app.get("/")
async def root() -> Dict[str, str]:
    return {"message": "Hello World"}

"""
Implements general settings for the app.
"""

from typing import Any, Dict

from dotenv import find_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    """
    General settings for the app.
    """

    debug: bool = True
    title: str = "Example API"
    version: str = "0.1.0"
    db_host: str
    db_user: str
    db_password: str
    db_name: str
    db_port: int

    model_config = SettingsConfigDict(
        extra="ignore",  # ignore any extra fields
        env_file=find_dotenv(".env"),
    )

    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        """
        Creates a dictionary with the FastAPI kwargs.
        :return:
        """
        return {
            "title": self.title,
            "version": self.version,
            "debug": self.debug,
        }

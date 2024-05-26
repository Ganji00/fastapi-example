"""
Configuration file for the project
"""
from functools import lru_cache

from src.core.settings.app import AppSettings


@lru_cache
def get_application_settings() -> AppSettings:
    """
    Gets application settings.
    :return: Application settings.
    """
    return AppSettings()

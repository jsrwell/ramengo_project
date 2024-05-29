"""
Configuration settings.
"""

# Lib Imports
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Base Settings of Project."""

    API_KEY: str = "ZtVdh8XQ2U8pWI2gmZ7f796Vh8GllXoN7mr0djNf"


settings = Settings()

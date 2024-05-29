"""
Configuration settings.
"""

# System Imports
import os

# Lib Imports
from pydantic_settings import BaseSettings
from dotenv import load_dotenv


# Load dotenv variables
load_dotenv()


class Settings(BaseSettings):
    """Base Settings of Project."""

    API_KEY: str = os.environ.get(
        "API_KEY", "ac5923cd4de19298ce7e2f9dfaa2014a4dd782b1")
    REDVENTURES_KEY: str = os.environ.get(
        "REDVENTURES_KEY", "ZtVdh8XQ2U8pWI2gmZ7f796Vh8GllXoN7mr0djNf")


settings = Settings()

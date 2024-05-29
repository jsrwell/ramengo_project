"""
Schemas for request and response models.
"""

# Lib Imports
from pydantic import BaseModel


class Broth(BaseModel):
    """
    Represents a broth option available in the RamenGo menu.
    """
    id: int
    imageInactive: str
    imageActive: str
    name: str
    description: str
    price: int


class Protein(BaseModel):
    """
    Represents a protein option available in the RamenGo menu.
    """
    id: int
    imageInactive: str
    imageActive: str
    name: str
    description: str
    price: int


class OrderRequest(BaseModel):
    """
    Represents a request to place an order in the RamenGo application.
    """
    brothId: str
    proteinId: str


class OrderResponse(BaseModel):
    """
    Represents the response after successfully placing an order.
    """
    id: str
    description: str
    image: str


class ErrorResponse(BaseModel):
    """
    Represents an error response returned by the API.
    """
    error: str

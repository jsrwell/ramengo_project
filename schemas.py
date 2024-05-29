"""
Schemas for request and response models.
"""

# Lib Imports
from pydantic import BaseModel


class Broth(BaseModel):
    id: int
    imageInactive: str
    imageActive: str
    name: str
    description: str
    price: int


class Protein(BaseModel):
    id: int
    imageInactive: str
    imageActive: str
    name: str
    description: str
    price: int


class OrderRequest(BaseModel):
    brothId: str
    proteinId: str


class OrderResponse(BaseModel):
    id: str
    description: str
    image: str


class ErrorResponse(BaseModel):
    error: str

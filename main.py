"""
Main module for RamenGo API.
"""

# System Imports
import json

# Lib Imports
import httpx
from fastapi.middleware.cors import CORSMiddleware
from fastapi import (
    FastAPI,
    HTTPException,
    Header,
    Request,
)
from pydantic import ValidationError

# Project Imports
from config import settings
from mocks import (
    BROTHS,
    PROTEINS,
)
from schemas import (
    OrderRequest,
    OrderResponse,
    Broth,
    Protein,
    ErrorResponse,
)

app = FastAPI()

# Allow CORS for any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/broths", response_model=list[Broth], tags=["Broths"])
def get_broths(x_api_key: str = Header(...)):
    """
    List all available broths.
    """
    if x_api_key != settings.API_KEY:
        raise HTTPException(status_code=403, detail="x-api-key header missing")
    return BROTHS


@app.get("/proteins", response_model=list[Protein], tags=["Proteins"])
def get_proteins(x_api_key: str = Header(...)):
    """
    List all available proteins.
    """
    if x_api_key != settings.API_KEY:
        raise HTTPException(status_code=403, detail="x-api-key header missing")
    return PROTEINS


@app.post("/order", response_model=OrderResponse, responses={
    201: {"description": "Order placed successfully", "model": OrderResponse},
    400: {"description": "Invalid request", "model": ErrorResponse},
    403: {"description": "Forbidden", "model": ErrorResponse},
    500: {"description": "Internal server error", "model": ErrorResponse},
}, tags=["Order"])
async def create_order(request: Request, x_api_key: str = Header(...)):
    """
    Place an order.
    """
    if x_api_key != settings.API_KEY:
        raise HTTPException(status_code=403, detail="x-api-key header missing")

    # Decoding JSON from request body
    try:
        order_data = await request.json()
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON body")

    try:
        order_request = OrderRequest(**order_data)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))

    broth = next(
        (item for item in
         BROTHS if item["id"] == int(order_request.brothId)), None)
    protein = next(
        (item for item in
         PROTEINS if item["id"] == int(order_request.proteinId)), None)

    if not broth or not protein:
        raise HTTPException(
            status_code=400, detail="both brothId and proteinId are required")

    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.tech.redventures.com.br/orders/generate-id",
            headers={"x-api-key": settings.API_KEY}
        )

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="could not place order")

    order_id = response.json().get("orderId")
    if not order_id:
        raise HTTPException(
            status_code=500, detail="Invalid order ID response")

    description = f"{broth['name']} and {protein['name']} Ramen"
    image_url = "https://tech.redventures.com.br/icons/ramen/ramenChasu.png"

    return OrderResponse(id=order_id, description=description, image=image_url)

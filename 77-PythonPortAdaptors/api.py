from adapters.sqlalchemy_inventory import SqlAlchemyInventoryAdapter
from db import get_db
from domain.errors import InvalidQuantity, OutOfStock, UnknownSku
from domain.models import OrderRequest
from domain.use_cases import place_order
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.engine import Connection

router = APIRouter()


class PlaceOrderIn(BaseModel):
    sku: str
    qty: int = Field(..., gt=0)


class PlaceOrderOut(BaseModel):
    sku: str
    qty: int
    remaining_stock: int

# Does 3 things : 1. parses input via pydantic model, 2. calls domain logic with port, 3. shapes output/domain errors with http responses.
@router.post("/orders", response_model=PlaceOrderOut)
def place_order_endpoint(
    payload: PlaceOrderIn,
    connection: Connection = Depends(get_db),
) -> PlaceOrderOut:
    try:
        result = place_order(
            OrderRequest(**payload.model_dump()),
            SqlAlchemyInventoryAdapter(conn=connection), # SQL Alchemy adapter implements the InventoryPort interface, so we can pass it to the domain logic without the domain logic needing to know anything about SQLAlchemy or the database.
        )
    except InvalidQuantity as e: # domain-level error, not tied to HTTP, so we translate it here into a 400 Bad Request.
        raise HTTPException(status_code=400, detail=str(e)) from e
    except UnknownSku as e:
        raise HTTPException(status_code=404, detail=str(e)) from e
    except OutOfStock as e:
        raise HTTPException(status_code=409, detail=str(e)) from e

    return PlaceOrderOut(
        sku=result.sku,
        qty=result.qty,
        remaining_stock=result.remaining_stock,
    )
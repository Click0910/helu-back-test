from pydantic import BaseModel
from uuid import UUID


class ItemCreateRequest(BaseModel):
    name: str
    description: str
    price: float
    quantity: int


class ItemResponse(BaseModel):
    id: UUID
    name: str
    description: str
    price: float
    quantity: int


class StockCheckResponse(BaseModel):
    available: bool
    current_stock: int

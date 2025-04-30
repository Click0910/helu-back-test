from pydantic import BaseModel
from uuid import UUID


class ItemStockRequest(BaseModel):
    item_id: UUID
    required_quantity: int


class ItemStockResponse(BaseModel):
    available: bool
    current_stock: int

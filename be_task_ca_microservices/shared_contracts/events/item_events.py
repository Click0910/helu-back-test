from pydantic import BaseModel
from uuid import UUID


class ItemReservedEvent(BaseModel):
    reservation_id: UUID
    user_id: UUID
    item_id: UUID
    quantity: int


class ItemOutOfStockEvent(BaseModel):
    item_id: UUID
    required_quantity: int

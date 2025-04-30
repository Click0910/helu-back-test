from dataclasses import dataclass
from uuid import UUID


@dataclass
class Item:
    id: UUID
    name: str
    description: str
    price: float
    available_quantity: int

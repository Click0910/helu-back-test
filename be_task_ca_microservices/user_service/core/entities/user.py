from dataclasses import dataclass
from uuid import UUID


@dataclass
class User:
    id: UUID
    email: str
    hashed_password: str
    first_name: str
    last_name: str
    cart_items: list['CartItem']

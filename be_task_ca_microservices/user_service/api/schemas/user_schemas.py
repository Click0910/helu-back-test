from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID


class UserCreateRequest(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str


class UserResponse(BaseModel):
    id: UUID
    email: EmailStr
    first_name: str
    last_name: str


class CartItemAddRequest(BaseModel):
    item_id: UUID
    quantity: int


class CartResponse(BaseModel):
    items: list[CartItemAddRequest]

from sqlalchemy import Column, UUID, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from uuid import uuid4
from ..session import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(512))
    first_name = Column(String(100))
    last_name = Column(String(100))

    cart_items = relationship("CartItemModel", back_populates="user")


class CartItemModel(Base):
    __tablename__ = "cart_items"

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), primary_key=True)
    item_id = Column(UUID(as_uuid=True), primary_key=True)  # ID reference to Item service
    quantity = Column(Integer)

    user = relationship("UserModel", back_populates="cart_items")

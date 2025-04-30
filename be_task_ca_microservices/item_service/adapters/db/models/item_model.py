from sqlalchemy import Column, UUID, String, Float, Integer
from uuid import uuid4
from ..session import Base


class ItemModel(Base):
    __tablename__ = "items"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(100), unique=True, index=True)
    description = Column(String(500))
    price = Column(Float)
    quantity = Column(Integer)

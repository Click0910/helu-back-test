from abc import ABC, abstractmethod
from uuid import UUID


class ItemClient(ABC):
    @abstractmethod
    def check_stock(self, item_id: UUID, quantity: int) -> bool: ...

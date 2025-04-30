from abc import ABC, abstractmethod


class EventPublisher(ABC):
    @abstractmethod
    def publish_reserved(self, item_id, quantity): ...

    @abstractmethod
    def publish_out_of_stock(self, item_id, quantity): ...
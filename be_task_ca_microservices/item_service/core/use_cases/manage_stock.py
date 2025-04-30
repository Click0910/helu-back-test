from dataclasses import dataclass
from core.contracts.event_publisher import EventPublisher


@dataclass
class ReserveStockUseCase:
    item_repository: 'ItemRepository'
    event_publisher: EventPublisher

    def execute(self, item_id: UUID, quantity: int):
        item = self.item_repository.get_by_id(item_id)

        if item.available_quantity < quantity:
            self.event_publisher.publish_out_of_stock(item_id, quantity)
            raise ValueError("Stock insuficiente")

        item.available_quantity -= quantity
        self.item_repository.save(item)
        self.event_publisher.publish_reserved(item_id, quantity)

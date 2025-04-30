import pika
from core.contracts.event_publisher import EventPublisher
from shared_contracts.events.item_events import ItemReservedEvent


class RabbitMQEventPublisher(EventPublisher):
    def __init__(self, connection_string: str):
        self.connection = pika.BlockingConnection(
            pika.URLParameters(connection_string)
        )
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='item_events')

    def publish_reserved(self, item_id, quantity):
        event = ItemReservedEvent(item_id=item_id, quantity=quantity)
        self.channel.basic_publish(
            exchange='',
            routing_key='item_events',
            body=event.json()
        )

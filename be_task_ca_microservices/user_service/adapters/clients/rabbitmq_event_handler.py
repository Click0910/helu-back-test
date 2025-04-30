import json
import pika
from uuid import UUID
from core.use_cases.add_to_cart import AddToCartUseCase


class CartSagaHandler:
    def __init__(self, use_case: AddToCartUseCase):
        self.use_case = use_case
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters('rabbitmq')
        )
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='cart_commands')

    def start_listening(self):
        self.channel.basic_consume(
            queue='cart_commands',
            on_message_callback=self.handle_message
        )
        self.channel.start_consuming()

    def handle_message(self, ch, method, properties, body):
        data = json.loads(body)
        try:
            self.use_case.execute(
                UUID(data['user_id']),
                UUID(data['item_id']),
                data['quantity']
            )
        except Exception as e:
            # Publish a compensating event or handle the error
            pass
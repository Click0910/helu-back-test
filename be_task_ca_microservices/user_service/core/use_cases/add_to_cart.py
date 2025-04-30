from uuid import UUID
from dataclasses import dataclass
from core.contracts.item_client import ItemClient


@dataclass
class AddToCartUseCase:
    item_client: ItemClient
    user_repository: 'UserRepository'

    def execute(self, user_id: UUID, item_id: UUID, quantity: int):
        # 1. Verificar stock usando el ItemClient (abstracto)
        if not self.item_client.check_stock(item_id, quantity):
            raise ValueError("Stock insuficiente")

        # 2. Actualizar carrito local
        user = self.user_repository.get_by_id(user_id)
        user.cart_items.append(CartItem(user_id, item_id, quantity))
        self.user_repository.save(user)

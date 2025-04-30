import requests
from core.contracts.item_client import ItemClient


class HTTPItemClient(ItemClient):
    def __init__(self, base_url: str):
        self.base_url = base_url

    def check_stock(self, item_id, quantity):
        response = requests.get(
            f"{self.base_url}/items/{item_id}/stock",
            params={"quantity": quantity}
        )
        return response.json()["available"]

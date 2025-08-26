import requests
from api_testing_practice.pet_store.objects.store_objects.base_order import BaseOrder

class CreateOrder(BaseOrder):

    def create_order(self, base_store_url, payload):
        self.response = requests.post(base_store_url, json=payload)
        self.response_json = self.response.json()



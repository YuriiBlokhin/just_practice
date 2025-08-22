import requests
from pet_store.objects.store_objects.base_order import BaseOrder


class DeleteOrder(BaseOrder):

    def delete_order(self, base_store_url, order_id):
        self.response = requests.delete(f'{base_store_url}/{order_id}')
        self.response_json = self.response.json()


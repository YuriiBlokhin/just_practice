import requests
from api_testing_practice.pet_store.objects.store_objects.base_order import BaseOrder

class GetOrder(BaseOrder):

    def get_order_by_id(self, base_store_url, order_id):
        self.response = requests.get(f'{base_store_url}/{order_id}')
        self.response_json = self.response.json()

    def check_response_id(self, order_id):
        assert self.response_json['id'] == order_id

    def check_response_404(self, order_id):
        assert self.response.status_code == 404
import requests
from pet_store.objects.pet_objects.base_pet import BaseEndpoint


class GetPet(BaseEndpoint):

    def get_pet_by_id(self, pet_base_url, pet_id):
        self.response = requests.get(f'{pet_base_url}/{pet_id}')
        self.response_json = self.response.json()

    def check_response_id(self, pet_id):
        assert self.response_json['id'] == pet_id

    def check_response_404(self, pet_id):
        assert self.response.status_code == 404
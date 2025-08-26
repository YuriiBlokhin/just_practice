import requests
from api_testing_practice.pet_store.objects.pet_objects.base_pet import BaseEndpoint


class DeletePet(BaseEndpoint):

    def delete_pet_by_id(self, pet_base_url, pet_id):
        self.response = requests.delete(f'{pet_base_url}/{pet_id}')
        self.response_json = self.response.json()


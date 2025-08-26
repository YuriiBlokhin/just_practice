import requests
from api_testing_practice.pet_store.objects.pet_objects.base_pet import BaseEndpoint


class CreateNewPet(BaseEndpoint):

    def create_new_pet(self, pet_base_url, pet_payload):
        self.response = requests.post(pet_base_url, json=pet_payload)
        self.response_json = self.response.json()

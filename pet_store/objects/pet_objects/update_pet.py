import requests
from pet_store.objects.pet_objects.base_endpoint import BaseEndpoint


class UpdatePet(BaseEndpoint):

    def update_pet(self, pet_base_url, pet_id, pet_update_payload):
        pet_update_payload['id'] = pet_id
        self.response = requests.put(pet_base_url, json=pet_update_payload)
        self.response_json = self.response.json()

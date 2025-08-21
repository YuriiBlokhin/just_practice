import requests
from rest_api.objects.base_endpoint import BaseEndpoint


class UpdateObject(BaseEndpoint):

    def update_objet_by_id(self, obj_id, update_payload):
        self.response = requests.put(
        f'https://api.restful-api.dev/objects/{obj_id}',
        json=update_payload
    )
        self.response_json = self.response.json()

    def check_response_name(self, name):
        assert self.response_json["name"] == name
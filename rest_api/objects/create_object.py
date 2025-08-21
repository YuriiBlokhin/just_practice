import requests
from rest_api.objects.base_endpoint import BaseEndpoint


class CreateObject(BaseEndpoint):

    def create_new_object(self, payload):
        self.response = requests.post('https://api.restful-api.dev/objects', json=payload)
        self.response_json = self.response.json()

    def check_response_name(self, name):
        assert self.response_json["name"] == name


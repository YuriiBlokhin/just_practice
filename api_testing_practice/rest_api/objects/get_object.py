import requests
from api_testing_practice.rest_api.objects.base_object import BaseEndpoint


class GetObject(BaseEndpoint):

    def get_object_by_id(self, obj_id):
        self.response = requests.get(f'https://api.restful-api.dev/objects/{obj_id}')
        self.response_json = self.response.json()

    def check_response_id(self, obj_id):
        assert self.response_json['id'] == obj_id

    def check_response_404(self, obj_id):
        assert self.response.status_code == 404
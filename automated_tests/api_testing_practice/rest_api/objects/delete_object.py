import requests
from automated_tests.api_testing_practice.rest_api.objects.base_object import BaseEndpoint


class DeleteObject(BaseEndpoint):

    def delete_object_by_id(self, obj_id):
        self.response = requests.delete(f'https://api.restful-api.dev/objects/{obj_id}')
        self.response_json = self.response.json()


import os
import requests
from automated_tests.api_testing_practice.go_rest.objects.base_user_object import BaseUser
from dotenv import load_dotenv

load_dotenv()


class CreateUser(BaseUser):

    def create_user(self, headers, payload):
        self.response = requests.post(f'{os.getenv('GOREST_BASE_URL')}', headers=headers, json=payload)
        self.response_json = self.response.json()

    def check_response_is_201(self):
        assert self.response.status_code == 201


import os
import requests
from dotenv import load_dotenv
from api_testing_practice.go_rest.objects.base_user_object import BaseUser

load_dotenv()

class UpdateUser(BaseUser):

    def update_user(self, user_id, headers, update_payload):
        self.response = requests.patch(
            f'{os.getenv('GOREST_BASE_URL')}/{user_id}', headers=headers, json=update_payload
                                  )
        self.response_json = self.response.json()

    def check_updated_name(self, update_payload):
        assert self.response_json['name'] == update_payload['name']

    def check_updated_email(self, update_payload):
        assert self.response_json['email'] == update_payload['email']

    def check_updated_status(self, update_payload):
        assert self.response_json['status'] == update_payload['status']
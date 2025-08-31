import os
import requests
from api_testing_practice.go_rest.objects.base_user_object import BaseUser
from dotenv import load_dotenv

load_dotenv()

class GetUsersList(BaseUser):

    def get_users_list(self, headers):
        self.response = requests.get(f'{os.getenv('GOREST_BASE_URL')}', headers=headers)
        self.response_json = self.response.json()

    def check_response_not_empty(self):
        assert len(self.response_json) > 0

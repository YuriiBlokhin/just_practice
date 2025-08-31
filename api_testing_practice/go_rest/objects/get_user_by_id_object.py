import os
import requests
from api_testing_practice.go_rest.objects.base_user_object import BaseUser
from dotenv import load_dotenv

load_dotenv()


class GetUserById(BaseUser):

    def get_user_by_id(self, user_id, headers):
        self.response = requests.get(f'{os.getenv('GOREST_BASE_URL')}/{user_id}', headers=headers)
        self.response_json = self.response.json()

    def check_response_is_404(self):
        assert self.response.status_code == 404
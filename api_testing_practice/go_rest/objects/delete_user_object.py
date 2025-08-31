import os
import requests
from api_testing_practice.go_rest.objects.base_user_object import BaseUser
from dotenv import load_dotenv

load_dotenv()


class DeleteUser(BaseUser):

    def delete_user(self, user_id, headers):
        self.response = requests.delete(f'{os.getenv('GOREST_BASE_URL')}/{user_id}', headers=headers)

    def check_response_is_204(self):
        assert self.response.status_code == 204
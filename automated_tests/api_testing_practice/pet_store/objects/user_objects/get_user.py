import requests
from automated_tests.api_testing_practice.pet_store.objects.user_objects.base_user import BaseUser

class GetUserById(BaseUser):

    def get_user_by_id(self, base_user_url, test_user):
        self.response = requests.get(f'{base_user_url}/{test_user}')
        self.response_json = self.response.json()

    def check_response_name(self, test_user):
        assert self.response_json['username'] == test_user

    def verify_user_is_deleted(self, base_user_url, test_user):
        self.response = requests.get(f'{base_user_url}/{test_user}')
        assert self.response.status_code == 404
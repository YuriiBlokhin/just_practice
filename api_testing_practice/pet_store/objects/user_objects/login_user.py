import requests
from api_testing_practice.pet_store.objects.user_objects.base_user import BaseUser

class LoginUser(BaseUser):

    def login_user(self, base_user_url, test_user, test_user_payload):
        self.response = requests.get(f'{base_user_url}/login', auth=(test_user, test_user_payload['password']))

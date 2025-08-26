import requests
from api_testing_practice.pet_store.objects.user_objects.base_user import BaseUser

class UpdateUser(BaseUser):

    def update_user(self, base_user_url, test_user, test_user_update_payload):
        self.response = requests.put(f'{base_user_url}/{test_user}', json=test_user_update_payload)


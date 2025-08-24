from pet_store.objects.user_objects.base_user import BaseUser
import requests


class CreateUser(BaseUser):

    def create_user(self, base_user_url, test_user_payload):
        self.response = requests.post(base_user_url, json=test_user_payload)


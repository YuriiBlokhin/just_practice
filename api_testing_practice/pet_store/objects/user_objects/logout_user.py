import requests
from api_testing_practice.pet_store.objects.user_objects.base_user import BaseUser


class LogoutUser(BaseUser):

    def logout_user(self, base_user_url):
        self.response = requests.get(f'{base_user_url}/logout')
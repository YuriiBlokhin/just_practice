from pet_store.objects.user_objects.base_user import BaseUser
import requests

class DeleteUser(BaseUser):

    def delete_user(self, base_user_url, test_user):
        self.response = requests.delete(f'{base_user_url}/{test_user}')


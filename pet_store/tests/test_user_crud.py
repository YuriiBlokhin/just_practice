import requests
from pet_store.objects.user_objects.create_user import CreateUser
from pet_store.objects.user_objects.delete_user import DeleteUser
from pet_store.objects.user_objects.get_user import GetUserById
from pet_store.objects.user_objects.login_user import LoginUser
from pet_store.objects.user_objects.logout_user import LogoutUser
from pet_store.objects.user_objects.update_user import UpdateUser


def test_create_user(base_user_url, test_user_payload):
    create_user_endpoint = CreateUser()
    create_user_endpoint.create_user(base_user_url, test_user_payload)
    create_user_endpoint.check_response_200()

def test_update_user(base_user_url, test_user, test_user_update_payload):
    update_user_endpoint = UpdateUser()
    update_user_endpoint.update_user(base_user_url, test_user, test_user_update_payload)
    update_user_endpoint.check_response_200()

def test_get_user_by_id(base_user_url, test_user):
    get_user_by_id_endpoint = GetUserById()
    get_user_by_id_endpoint.get_user_by_id(base_user_url, test_user)
    get_user_by_id_endpoint.check_response_name(test_user)

def test_login_user(base_user_url, test_user, test_user_payload):
    login_user_endpoint = LoginUser()
    login_user_endpoint.login_user(base_user_url, test_user, test_user_payload)
    login_user_endpoint.check_response_200()

def test_logout_user(base_user_url, test_user, test_user_payload):
    login_user_endpoint = LoginUser()
    login_user_endpoint.login_user(base_user_url, test_user, test_user_payload)
    login_user_endpoint.check_response_200()
    logout_user_endpoint = LogoutUser()
    logout_user_endpoint.logout_user(base_user_url)
    logout_user_endpoint.check_response_200()

def test_delete_user(base_user_url, test_user):
    delete_user_endpoint = DeleteUser()
    delete_user_endpoint.delete_user(base_user_url, test_user)
    delete_user_endpoint.check_response_200()
    verify_user_is_deleted = GetUserById()
    verify_user_is_deleted.verify_user_is_deleted(base_user_url, test_user)
    verify_user_is_deleted.check_response_404()
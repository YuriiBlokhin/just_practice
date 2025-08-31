import pytest
import requests
from api_testing_practice.go_rest.test_data.headers import headers
from api_testing_practice.go_rest.test_data.payloads import post_payload, patch_payload


@pytest.fixture()
def authorization():
    return headers

@pytest.fixture()
def payload():
    return post_payload()

@pytest.fixture()
def update_payload():
    return patch_payload()

@pytest.fixture(scope="function")
def user_id(authorization, payload):
    response = requests.post('https://gorest.co.in/public/v2/users', headers=authorization, json=payload).json()
    yield response['id']
    requests.delete(f'https://gorest.co.in/public/v2/users/{response["id"]}', headers=authorization)

@pytest.fixture(scope="function")
def user_id_for_update_user(authorization, update_payload):
    response = requests.post('https://gorest.co.in/public/v2/users', headers=authorization, json=update_payload).json()
    yield response['id']
    requests.delete(f'https://gorest.co.in/public/v2/users/{response["id"]}', headers=authorization)

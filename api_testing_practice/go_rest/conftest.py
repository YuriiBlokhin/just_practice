import pytest
import requests
from api_testing_practice.go_rest.test_data.headers import headers
from api_testing_practice.go_rest.test_data.payloads import post_payload, patch_payload
import os
from dotenv import load_dotenv
load_dotenv()


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
    response = requests.post(f'{os.getenv('GOREST_BASE_URL')}', headers=authorization, json=payload).json()
    yield response['id']
    requests.delete(f'{os.getenv('GOREST_BASE_URL')}/{response["id"]}', headers=authorization)

@pytest.fixture(scope="function")
def user_id_for_update_user(authorization, update_payload):
    response = requests.post(f'{os.getenv('GOREST_BASE_URL')}', headers=authorization, json=update_payload).json()
    yield response['id']
    requests.delete(f'{os.getenv('GOREST_BASE_URL')}/{response["id"]}', headers=authorization)

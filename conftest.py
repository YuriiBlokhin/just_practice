import pytest
import json
import os
from dotenv import load_dotenv
import requests

from pet_store.objects.pet_objects.create_pet import CreateNewPet
from pet_store.objects.pet_objects.delete_pet import DeletePet
from rest_api.objects.create_object import CreateObject
from rest_api.objects.delete_object import DeleteObject

load_dotenv()

# rest_api_fixtures
@pytest.fixture()
def payload():
    return json.loads(os.getenv("payload"))

@pytest.fixture()
def update_payload():
    return json.loads(os.getenv("update_payload"))

@pytest.fixture()
def obj_id(payload):
    test_object = CreateObject()
    test_object.create_new_object(payload)
    yield test_object.response_json['id']
    delete_test_object = DeleteObject()
    delete_test_object.delete_object_by_id(test_object.response_json['id'])


# pet_store_fixtures
@pytest.fixture()
def pet_payload():
    return json.loads(os.getenv("pet_payload"))

@pytest.fixture()
def pet_update_payload():
    # pet_id = os.getenv("pet_id")
    return json.loads(os.getenv("pet_update_payload"))

@pytest.fixture()
def pet_id (pet_base_url, pet_payload):
    test_pet = CreateNewPet()
    test_pet.create_new_pet(pet_base_url, pet_payload)
    yield test_pet.response_json['id']
    delete_test_pet = DeletePet()
    delete_test_pet.delete_pet_by_id(pet_base_url, test_pet.response_json['id'])

@pytest.fixture()
def pet_base_url():
    return os.getenv('pet_base_url')

# store fixtures
@pytest.fixture()
def order_id(base_store_url, payload):
    response = requests.post(base_store_url, json=payload).json()
    return response['id']
    # response = requests.delete(f'https://petstore.swagger.io/v2/store/order/{response["id"]}')

@pytest.fixture()
def base_store_url():
    return os.getenv('base_store_url')

# user fixtures
@pytest.fixture()
def test_user(base_user_url, test_user_payload):
    response = requests.post(base_user_url, json=test_user_payload).json()
    yield test_user_payload['username']
    response = requests.delete(f"{base_user_url}/{test_user_payload['username']}")

@pytest.fixture()
def base_user_url():
    return os.getenv('base_user_url')

@pytest.fixture()
def test_user_payload():
    return json.loads(os.getenv("user_payload"))

@pytest.fixture()
def test_user_update_payload():
    return json.loads(os.getenv("user_update_payload"))
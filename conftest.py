import pytest
import json
import os
from dotenv import load_dotenv
import requests
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
def pet_id ():
    payload = {
        "id": 0,
        "category": {
            "id": 0,
            "name": "lama"
        },
        "name": "rousvelt",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }
    response = requests.post('https://petstore.swagger.io/v2/pet', json=payload).json()
    return response['id']


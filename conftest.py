import pytest
import json
import os
from dotenv import load_dotenv
import requests

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
    response = requests.post('https://api.restful-api.dev/objects', json=payload).json()
    yield response['id']
    requests.delete(f'https://api.restful-api.dev/objects/{response["id"]}')

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


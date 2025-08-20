import pytest
import json
import os
from dotenv import load_dotenv
import requests

load_dotenv()

@pytest.fixture()
def payload():
    return json.loads(os.getenv("payload"))


@pytest.fixture()
def obj_id(payload):
    response = requests.post('https://api.restful-api.dev/objects', json=payload).json()
    yield response['id']
    requests.delete(f'https://api.restful-api.dev/objects/{response["id"]}')

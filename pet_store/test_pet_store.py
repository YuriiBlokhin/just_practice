import requests
import time


def test_create_pet():
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
    assert response['name'] == payload['name']


def test_get_pet(pet_id):
    time.sleep(3) # for sure server have enough time to create an object
    response = requests.get(f'https://petstore.swagger.io/v2/pet/{pet_id}').json()
    assert response['id'] == pet_id


def test_update_pet(pet_id):
    payload = {
      "id": pet_id,
      "category": {
        "id": 0,
        "name": "poni"
      },
      "name": "koni",
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

    response = requests.put(f'https://petstore.swagger.io/v2/pet', json=payload).json()
    assert response['name'] == payload['name']

def test_delete_pet(pet_id):
    time.sleep(3) # for sure server have enough time to create an object
    response = requests.delete(f'https://petstore.swagger.io/v2/pet/{pet_id}')
    assert response.status_code == 200
    response = requests.get(f'https://petstore.swagger.io/v2/pet/{pet_id}')
    assert response.status_code == 404



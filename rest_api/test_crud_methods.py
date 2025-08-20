import requests

def test_create_object(payload):
    response = requests.post('https://api.restful-api.dev/objects', json=payload).json()
    assert response["name"] == payload["name"]


def test_get_object(obj_id):
    response = requests.get(f'https://api.restful-api.dev/objects/{obj_id}').json()
    assert response['id'] == obj_id


def test_update_object(obj_id, payload):
    response = requests.put(
        f'https://api.restful-api.dev/objects/{obj_id}',
        json=payload
    ).json()
    assert response["name"] == payload["name"]


def test_delete_object(obj_id):
    response = requests.delete(f'https://api.restful-api.dev/objects/{obj_id}')
    assert response.status_code == 200
    response = requests.get(f'https://api.restful-api.dev/objects/{obj_id}')
    assert response.status_code == 404



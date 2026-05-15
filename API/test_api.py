import requests
import pytest


@pytest.fixture()
def id_object():
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.post('https://api.restful-api.dev/objects',
                             headers={'Content-Type': 'application/json'},
                             json=payload)
    id_object = response.json()['id']
    yield response.json()['id']
    requests.delete(f'https://api.restful-api.dev/objects/{id_object}')

def test_create_user():
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.post('https://api.restful-api.dev/objects',
                             headers={'Content-Type': 'application/json'},
                             json=payload)
    print(response.json()['id'])
    assert response.json()['name'] == payload['name']


def test_get_user(id_object):
    response = requests.get(f'https://api.restful-api.dev/objects/{id_object}')
    print(id_object)
    assert response.status_code == 200


def test_update_user(id_object):
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2026,
            "price": 2000,
            "CPU model": "Intel Core i9",
            "Hard disk size": "2 TB"
        }
    }
    response = requests.put(f'https://api.restful-api.dev/objects/{id_object}',
                            json=payload,
                            headers={'Content-Type': 'application/json'})
    assert response.status_code == 200
    print(id_object)
# вроде как начал разбираться с гитом



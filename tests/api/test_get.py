import requests
from jsonschema.validators import validate
from schemas import get_single_user

base_url = "https://reqres.in"


def test_get_list_user():
    response = requests.get(base_url + "/api/users?page=2")
    assert response.status_code == 200


def test_get_single_user():
    response = requests.get(base_url + "/api/users/2")
    assert response.status_code == 200
    body = response.json()
    validate(body, get_single_user)




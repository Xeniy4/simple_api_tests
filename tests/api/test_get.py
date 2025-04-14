from http.client import responses

import requests
from jsonschema.validators import validate
from schemas import get_single_user

base_url = "https://reqres.in"
endpoint_list_users = "/api/users?page=2"
endpoint_single_user = "/api/users/2"
endpoint_not_found_user = "/api/users/23"


def test_get_list_users():
    response = requests.get(base_url + endpoint_list_users)
    assert response.status_code == 200


def test_get_single_user():
    response = requests.get(base_url + endpoint_single_user)
    assert response.status_code == 200
    body = response.json()
    validate(body, get_single_user)


def test_get_not_found_user():
    response = requests.get(base_url + endpoint_not_found_user)
    assert response.status_code == 404





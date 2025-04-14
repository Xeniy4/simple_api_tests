from http.client import responses

import requests
from jsonschema.validators import validate
from schemas import post_create_user

base_url = "https://reqres.in"
endpoint_update = "/api/users/2"

body_update = {
    "name": "Tom",
    "job": "zion resident"
}

def test_put_user():
    response = requests.put(base_url + endpoint_update, data=body_update)
    assert response.status_code == 200




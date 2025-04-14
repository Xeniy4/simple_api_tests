from functools import reduce
from http.client import responses

import requests
from jsonschema.validators import validate
from schemas import post_create_user, post_register_user, post_register_user_400, post_register_user_unsuccessful

base_url = "https://reqres.in"

endpoint_create = "/api/users"
endpoint_register = "/api/register"

body_create = {
    "name": "Tom",
    "job": "doctor"
}

body_register_400 = {
    "email": "tom_doct@test.com",
    "password": "tom123456"
}

body_register = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

body_register_unsuccessful = {
    "password": "pistol"
}


def test_post_create():
    response = requests.post(base_url + endpoint_create, data=body_create)
    assert response.status_code == 201
    assert response.json()["name"] == "Tom"
    assert response.json()["job"] == "doctor"
    response_body = response.json()
    validate(response_body, post_create_user)


def test_post_register():
    response = requests.post(base_url + endpoint_register, data=body_register)
    assert response.status_code == 200
    response_body = response.json()
    validate(response_body, post_register_user)


def test_post_register_negative():
    response = requests.post(base_url + endpoint_register, data=body_register_400)
    assert response.status_code == 400
    response_body = response.json()
    validate(response_body, post_register_user_400)


def test_post_register_miss_email_negative():
    response = requests.post(base_url + endpoint_register, data=post_register_user_unsuccessful)
    assert response.status_code == 400
    assert response.json()["error"] == "Missing email or username"
    response_body = response.json()
    validate(response_body, body_register_unsuccessful)

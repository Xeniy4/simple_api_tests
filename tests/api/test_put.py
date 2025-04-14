from http.client import responses

import requests
from jsonschema.validators import validate
from schemas import put_update_user

base_url = "https://reqres.in"
endpoint_update = "/api/users/2"

body_update = {
    "name": "Tom",
    "job": "zion resident"
}

def test_put_user():
    response = requests.put(base_url + endpoint_update, data=body_update)
    assert response.status_code == 200
    assert response.json()["job"] == "zion resident"
    response_body = response.json()
    validate(response_body, put_update_user)

def test_put_user_negative():
    pass
# добавить изменение имени в боди, и еще что-нибудь
# изменить имя или работу невалидными значениями




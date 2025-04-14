from http.client import responses

import requests

base_url = "https://reqres.in"
endpoint_user = "/api/users/2"


def test_delete_user():
    response_delete = requests.delete(base_url + endpoint_user)
    assert response_delete.status_code == 204
    response_get = requests.get(base_url + endpoint_user)
    assert response_get.status_code == 200
'''В последней строчке по идее должно быть status_code == 404, т.к. юзера удалили, 
но на этом тестовом сайте юзеры не удаляются'''

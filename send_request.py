import requests

import configuration
import data


def create_token():
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, json=data.USER_BODY, headers=data.headers)
    authToken = 'Bearer ' + response.json()["authToken"]
    return authToken

def create_headers(key, value):
    token = data.HEADERS_KIT.copy()
    token[key] = value
    return token

def create_kit(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
                             headers=create_headers('Authorization', create_token()),
                             json=body)


def get_kit_body():
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH, headers = data.HEADERS_KIT, json=data.KIT_BODY)
    return response.json()
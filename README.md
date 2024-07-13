# Тесты на проверку параметра 'name' при создании набора пользователя в Яндекс.Прилавок с помощью API Яндекс.Прилавок.
### - Для запуска тестов должны быть установлены пакеты pytest и requests
### - Запуск всех тестов выполянется командой pytest

## ![v2](https://github.com/GorgeousTV/Pytest-API-Yandex.Prilavok/assets/144271169/be815888-48c0-4312-9b33-694ba8829463) Файл конфигурации

``URL_SERVICE = "https://55324992-6e7b-4b1e-927e-dbb3f5a6e059.serverhub.praktikum-services.ru"
DOC_PATH = "/docs/"
CREATE_USER_PATH = "/api/v1/users/"
CREATE_KIT_PATH = "/api/v1/kits"``

## ![v2](https://github.com/GorgeousTV/Pytest-API-Yandex.Prilavok/assets/144271169/be815888-48c0-4312-9b33-694ba8829463) Файл с заголовками и телами запросов


``
headers = {
    "Content-Type": "application/json"
}

HEADERS_KIT = {
    "Content-Type": "application/json",
    "Authorization": "Bearer jknnFApafP4awfAIFfafam2fma"
}


USER_BODY = {
    "firstName": "Анатолий",
    "phone": "+79995553322",
    "address": "г. Москва, ул. Пушкина, д. 10"
}

KIT_BODY = {
       "name": "Мой набор"
}
``

## ![v2](https://github.com/GorgeousTV/Pytest-API-Yandex.Prilavok/assets/144271169/be815888-48c0-4312-9b33-694ba8829463) Файл с реквестами

``
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
``

## ![v2](https://github.com/GorgeousTV/Pytest-API-Yandex.Prilavok/assets/144271169/be815888-48c0-4312-9b33-694ba8829463) Файл с тестами

``
import data
import send_request


def modify_create_name_kit(key, value):
    body = data.KIT_BODY.copy()
    body[key] = value
    return body

def positive_assert(key, value):
    kit_body = modify_create_name_kit(key, value)
    kit_response = send_request.create_kit(kit_body)

    assert kit_response.status_code == 201
    assert kit_response.json()['name'] == value

def negative_assert(key, value):
    kit_body = modify_create_name_kit(key, value)
    response = send_request.create_kit(kit_body)
    assert response.status_code == 400
    assert response.json()['code'] == 400
    assert response.json()['message'] == "Не все необходимые параметры были переданы"

def no_name_assert():
    body = data.KIT_BODY.copy()
    body.pop('name')
    return body

def negative_assert_no_name_kit():
    kit_body = no_name_assert()
    response = send_request.create_kit(kit_body)
    assert response.status_code == 400
    assert response.json()['message'] == "Не все необходимые параметры были переданы"

def test_create_kit_with_name_one_symbol():
    positive_assert('name', 'N')

def test_create_kit_with_name_max_symbol():
    positive_assert('name', 'AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC')

def test_create_kit_empty_name_symbol():
    negative_assert('name', '')

def test_create_kit_max_plus_one_more_name_symbol():
    negative_assert('name', 'AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD')

def test_create_kit_eng_symbol():
    positive_assert('name', 'QWErty')

def test_create_kit_rus_symbol():
    positive_assert('name', 'Мария')

def test_create_kit_with_spec_symbol():
    positive_assert('name', '"№%@",')

def test_create_kit_with_spaces():
    positive_assert('name', ' Человек и КО ')

def test_create_kit_with_numbers():
    positive_assert('name', '123')

def test_create_kit_with_type_int_key_value():
    negative_assert('name', 123)

def test_create_kit_no_name():
    negative_assert_no_name_kit()
``

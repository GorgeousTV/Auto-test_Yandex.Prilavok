import send_request
import requests
import data

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
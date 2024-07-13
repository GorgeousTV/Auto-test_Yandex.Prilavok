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

![реквесты](https://github.com/GorgeousTV/Pytest-API-Yandex.Prilavok/assets/144271169/1066862e-ad67-40b2-a12e-ba3e963d2b0b)

## ![v2](https://github.com/GorgeousTV/Pytest-API-Yandex.Prilavok/assets/144271169/be815888-48c0-4312-9b33-694ba8829463) Файл с тестами

![создание_тестов](https://github.com/GorgeousTV/Pytest-API-Yandex.Prilavok/assets/144271169/114c6bac-90c5-4e6c-b6e1-28a96634f9db)

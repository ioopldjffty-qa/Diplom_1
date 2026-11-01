import sys
import os
import pytest
import requests
import random
import string
import allure

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from helpers import register_user, delete_user

@allure.step("Генерация случайной строки")
def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

@pytest.fixture
def create_user():
    email = f"test_{generate_random_string(10)}@yandex.ru"
    password = generate_random_string(10)
    name = generate_random_string(10)

    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    response = register_user(payload)
    access_token = response.json().get("accessToken")

    yield response, payload

    # ОЧИСТКА
    if access_token:
        headers = {"Authorization": access_token}
        delete_user(headers)

@pytest.fixture
def auth_headers(create_user):
    response, payload = create_user
    access_token = response.json().get("accessToken")
    return {"Authorization": access_token}
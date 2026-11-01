import requests
import allure
from data import BASE_URL

@allure.step("Отправляем запрос на регистрацию пользователя")
def register_user(payload):
    return requests.post(f"{BASE_URL}/api/auth/register", data=payload)

@allure.step("Отправляем запрос на авторизацию пользователя")
def login_user(payload):
    return requests.post(f"{BASE_URL}/api/auth/login", data=payload)

@allure.step("Отправляем запрос на создание заказа")
def create_order(payload, headers=None):
    return requests.post(f"{BASE_URL}/api/orders", json=payload, headers=headers)

@allure.step("Отправляем запрос на удаление пользователя")
def delete_user(headers):
    return requests.delete(f"{BASE_URL}/api/auth/user", headers=headers)
import allure
import pytest
from helpers import login_user
from data import MSG_WRONG_CREDENTIALS


@allure.suite("Авторизация пользователя")
class TestLoginUser:

    @allure.title("Успешный вход существующего пользователя")
    def test_login_existing_user(self, create_user):
        response, payload = create_user
        login_payload = {
            "email": payload["email"],
            "password": payload["password"]
        }
        login_response = login_user(login_payload)
        assert login_response.status_code == 200

    @allure.title("Проверка наличия токена при успешном входе")
    def test_login_existing_user_has_token(self, create_user):
        response, payload = create_user
        login_payload = {
            "email": payload["email"],
            "password": payload["password"]
        }
        login_response = login_user(login_payload)
        assert login_response.json().get("accessToken") is not None

    @allure.title("Вход с неверными данными возвращает код 401")
    def test_login_wrong_credentials_status(self):
        login_payload = {
            "email": "wrong_email@yandex.ru",
            "password": "wrong_password"
        }
        response = login_user(login_payload)
        assert response.status_code == 401

    @allure.title("Сообщение при неверных данных авторизации")
    def test_login_wrong_credentials_message(self):
        login_payload = {
            "email": "wrong_email@yandex.ru",
            "password": "wrong_password"
        }
        response = login_user(login_payload)
        assert response.json().get("message") == MSG_WRONG_CREDENTIALS
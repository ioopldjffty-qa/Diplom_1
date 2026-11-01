import allure
import pytest
from helpers import register_user
from conftest import generate_random_string
from data import MSG_USER_ALREADY_EXISTS, MSG_REQUIRED_FIELDS

@allure.suite("Создание пользователя")
class TestCreateUser:

    @allure.title("Успешное создание уникального пользователя")
    def test_create_unique_user_success(self):
        payload = {
            "email": f"test_{generate_random_string(10)}@yandex.ru",
            "password": generate_random_string(10),
            "name": generate_random_string(10)
        }
        response = register_user(payload)
        assert response.status_code == 200

    @allure.title("Проверка ответа при успешной регистрации")
    def test_create_unique_user_response(self):
        payload = {
            "email": f"test_{generate_random_string(10)}@yandex.ru",
            "password": generate_random_string(10),
            "name": generate_random_string(10)
        }
        response = register_user(payload)
        assert response.json().get("success") is True

    @allure.title("Создание дубликата пользователя возвращает код 403")
    def test_create_duplicate_user_status(self, create_user):
        response, payload = create_user
        duplicate_response = register_user(payload)
        assert duplicate_response.status_code == 403

    @allure.title("Сообщение при создании дубликата пользователя")
    def test_create_duplicate_user_message(self, create_user):
        response, payload = create_user
        duplicate_response = register_user(payload)
        assert duplicate_response.json().get("message") == MSG_USER_ALREADY_EXISTS

    @allure.title("Создание пользователя без пароля возвращает код 403")
    def test_create_user_without_password_status(self):
        payload = {
            "email": f"test_{generate_random_string(10)}@yandex.ru",
            "name": generate_random_string(10)
        }
        response = register_user(payload)
        assert response.status_code == 403

    @allure.title("Сообщение при создании пользователя без пароля")
    def test_create_user_without_password_message(self):
        payload = {
            "email": f"test_{generate_random_string(10)}@yandex.ru",
            "name": generate_random_string(10)
        }
        response = register_user(payload)
        assert response.json().get("message") == MSG_REQUIRED_FIELDS
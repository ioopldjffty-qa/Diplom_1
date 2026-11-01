import allure
from helpers import create_order
from data import INGREDIENT_HASH_1, INGREDIENT_HASH_2, INVALID_INGREDIENT_HASH, MSG_NEED_AUTH, MSG_NEED_INGREDIENTS

@allure.suite("Создание заказа")
class TestCreateOrder:

    @allure.title("Создание заказа с авторизацией")
    def test_create_order_with_auth(self, auth_headers):
        payload = {"ingredients": [INGREDIENT_HASH_1, INGREDIENT_HASH_2]}
        response = create_order(payload, auth_headers)
        assert response.status_code == 200

    @allure.title("Создание заказа без авторизации (разрешено API)")
    def test_create_order_without_auth(self):
        payload = {"ingredients": [INGREDIENT_HASH_1]}
        response = create_order(payload)
        assert response.status_code == 200

    @allure.title("Создание заказа с большим количеством ингредиентов")
    def test_create_order_with_ingredients(self, auth_headers):
        payload = {"ingredients": [INGREDIENT_HASH_1, INGREDIENT_HASH_2]}
        response = create_order(payload, auth_headers)
        assert response.status_code == 200

    @allure.title("Создание заказа без ингредиентов возвращает 400")
    def test_create_order_without_ingredients(self, auth_headers):
        payload = {"ingredients": []}
        response = create_order(payload, auth_headers)
        assert response.status_code == 400

    @allure.title("Сообщение при создании заказа без ингредиентов")
    def test_create_order_without_ingredients_message(self, auth_headers):
        payload = {"ingredients": []}
        response = create_order(payload, auth_headers)
        assert response.json().get("message") == MSG_NEED_INGREDIENTS

    @allure.title("Создание заказа с неверным хешем ингредиента")
    def test_create_order_with_invalid_ingredient_hash(self, auth_headers):
        payload = {"ingredients": [INVALID_INGREDIENT_HASH]}
        response = create_order(payload, auth_headers)
        assert response.status_code == 500
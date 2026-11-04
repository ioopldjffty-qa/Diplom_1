import pytest
from unittest.mock import Mock

from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestBurger:

    def test_set_buns(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100

        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    def test_add_ingredient_count(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = "hot sauce"

        burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == 1

    def test_add_ingredient_content(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = "hot sauce"

        burger.add_ingredient(mock_ingredient)

        assert burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient_count(self):
        burger = Burger()
        mock_ingredient1 = Mock()
        mock_ingredient2 = Mock()
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 1

    def test_remove_ingredient_content(self):
        burger = Burger()
        mock_ingredient1 = Mock()
        mock_ingredient2 = Mock()
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        burger.remove_ingredient(0)

        assert burger.ingredients[0] == mock_ingredient2

    def test_move_ingredient_first_element(self):
        burger = Burger()
        mock_ingredient1 = Mock()
        mock_ingredient2 = Mock()
        mock_ingredient3 = Mock()
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.add_ingredient(mock_ingredient3)

        burger.move_ingredient(0, 2)

        assert burger.ingredients[0] == mock_ingredient2

    def test_move_ingredient_second_element(self):
        burger = Burger()
        mock_ingredient1 = Mock()
        mock_ingredient2 = Mock()
        mock_ingredient3 = Mock()
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.add_ingredient(mock_ingredient3)

        burger.move_ingredient(0, 2)

        assert burger.ingredients[1] == mock_ingredient3

    def test_move_ingredient_third_element(self):
        burger = Burger()
        mock_ingredient1 = Mock()
        mock_ingredient2 = Mock()
        mock_ingredient3 = Mock()
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.add_ingredient(mock_ingredient3)

        burger.move_ingredient(0, 2)

        assert burger.ingredients[2] == mock_ingredient1

    def test_get_price(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100
        burger.set_buns(mock_bun)

        mock_ingredient1 = Mock()
        mock_ingredient1.get_price.return_value = 50
        mock_ingredient2 = Mock()
        mock_ingredient2.get_price.return_value = 75
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        expected_price = 100 * 2 + 50 + 75
        assert burger.get_price() == expected_price

    @pytest.mark.parametrize("ingredients_count, expected_price", [
        (0, 200),
        (1, 300),
        (2, 400),
    ])
    def test_get_price_with_different_ingredients_count(self, ingredients_count, expected_price):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100
        burger.set_buns(mock_bun)

        for _ in range(ingredients_count):
            mock_ingredient = Mock()
            mock_ingredient.get_price.return_value = 100
            burger.add_ingredient(mock_ingredient)

        assert burger.get_price() == expected_price

    def test_get_receipt(self):
        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100
        burger.set_buns(mock_bun)

        mock_ingredient1 = Mock()
        mock_ingredient1.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient1.get_name.return_value = "hot sauce"
        mock_ingredient1.get_price.return_value = 100

        mock_ingredient2 = Mock()
        mock_ingredient2.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ingredient2.get_name.return_value = "cutlet"
        mock_ingredient2.get_price.return_value = 100

        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        expected_receipt = (
            "(==== black bun ====)\n"
            "= sauce hot sauce =\n"
            "= filling cutlet =\n"
            "(==== black bun ====)\n"
            "\n"
            "Price: 400"
        )
        assert burger.get_receipt() == expected_receipt

    def test_get_receipt_without_ingredients(self):
        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100
        burger.set_buns(mock_bun)

        expected_receipt = (
            "(==== black bun ====)\n"
            "(==== black bun ====)\n"
            "\n"
            "Price: 200"
        )
        assert burger.get_receipt() == expected_receipt
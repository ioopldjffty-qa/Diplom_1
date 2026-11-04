from praktikum.database import Database

class TestDatabase:

    def test_available_buns_count(self):
        db = Database()
        buns = db.available_buns()
        assert len(buns) == 3

    def test_available_buns_first_name(self):
        db = Database()
        buns = db.available_buns()
        assert buns[0].get_name() == "black bun"

    def test_available_buns_second_name(self):
        db = Database()
        buns = db.available_buns()
        assert buns[1].get_name() == "white bun"

    def test_available_buns_third_name(self):
        db = Database()
        buns = db.available_buns()
        assert buns[2].get_name() == "red bun"

    def test_available_ingredients_count(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6

    def test_available_ingredients_first_name(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert ingredients[0].get_name() == "hot sauce"

    def test_available_ingredients_second_name(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert ingredients[1].get_name() == "sour cream"

    def test_available_ingredients_third_name(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert ingredients[2].get_name() == "chili sauce"

    def test_available_ingredients_fourth_name(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert ingredients[3].get_name() == "cutlet"

    def test_available_ingredients_fifth_name(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert ingredients[4].get_name() == "dinosaur"

    def test_available_ingredients_sixth_name(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert ingredients[5].get_name() == "sausage"
import random
import string

class Generator:

    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for _ in range(length))
        return random_string

    @staticmethod
    def generate_random_email(length):
        characters = string.digits
        digits = ''.join(random.choice(characters) for _ in range(length))
        return f"test_user_{digits}@ya.ru"
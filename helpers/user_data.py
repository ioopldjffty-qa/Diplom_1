import random
import string
import uuid


EMAIL_DOMAIN = "yandex.ru"
PASSWORD_LENGTH = 10


def generate_email():
    return f"test_{uuid.uuid4().hex[:10]}@{EMAIL_DOMAIN}"


def generate_password(length=PASSWORD_LENGTH):
    symbols = string.ascii_letters + string.digits
    return "".join(random.choices(symbols, k=length))


def generate_name():
    return f"User{random.randint(1000, 9999)}"


def generate_user_data():
    return {
        "email": generate_email(),
        "password": generate_password(),
        "name": generate_name(),
    }
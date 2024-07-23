import requests
import random
import string
import allure
from data import Url


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


@allure.step(f'Генерируем данные для регистрации с рандомным емаилом')
def new_user_data():
    user_data = {
        "email": f'{generate_random_string}@landex.ru',
        "password": "qwerty_angel",
        "name": "anastasia_angel"
    }
    return user_data


@allure.step(f'Генерируем данные для регистрации')
def registration_user_full_data():
    email = f'{generate_random_string(10)}@email.ru'
    password = generate_random_string(10)
    name = generate_random_string(10)

    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    # возвращаем список
    return payload


@allure.step(f'Регистрируем пользователя, возвращаем данные для логина')
def registration_user_get_data_for_login():
    email = f'{generate_random_string(10)}@email.ru'
    password = generate_random_string(10)
    name = generate_random_string(10)

    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    response = requests.post(Url.url_create_user, data=payload)

    login_pass = {}

    # если регистрация прошла успешно (код ответа 201), добавляем данные для логина
    if response.status_code == 200:
        login_pass["email"] = email
        login_pass["password"] = password

    # возвращаем список
    return login_pass


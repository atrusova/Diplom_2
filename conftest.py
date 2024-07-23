import pytest
import requests
from data import Url
from helpers import registration_user_get_data_for_login


@pytest.fixture(scope="module")
def logged_in_user():
    # Регистрация и логин пользователя
    login_data = registration_user_get_data_for_login()
    response_login = requests.post(Url.url_login_user, data=login_data)
    r = response_login.json()
    token_full_string = r["accessToken"]
    token = token_full_string.split()[1]

    yield token  # Возвращает токен для использования в тестах

    # Удаление пользователя после завершения теста
    requests.delete(Url.url_delete_user, headers={'Authorization': f'Bearer {token}'})

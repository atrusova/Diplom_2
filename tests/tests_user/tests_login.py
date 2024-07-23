import pytest
import requests
import allure
import json
from data import Url, TextsError
from helpers import registration_user_get_data_for_login, generate_random_string


class TestLogin:

    @allure.title(f'Проверка успешного логина пользователя')
    def test_login_user_exist_status_200_get_token(self):
        login_data = registration_user_get_data_for_login()
        response = requests.post(Url.url_login_user, data=login_data)
        r = response.json()
        token_full_string = r["accessToken"]
        token = token_full_string.split()[1]
        requests.delete(Url.url_delete_user, headers={'Authorization': f'Bearer {token}'})

        assert response.status_code == 200 and r["accessToken"] is not None

    @pytest.mark.parametrize(
        'field, value',
        [
            ("email", generate_random_string),
            ("password", generate_random_string)
        ]
    )
    @allure.title(f'Проверка логина с неверным логином или паролем')
    def test_login_incorrect_data_status_401_get_message_incorrect_data(self, field, value):
        login_data = registration_user_get_data_for_login()
        login_data[field] = value
        response = requests.post(Url.url_login_user, data=login_data)
        r = response.json()

        assert response.status_code == 401 and r["message"] == TextsError.incorrect_data_for_login

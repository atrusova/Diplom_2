import pytest
import requests
import allure
import json
from data import Url, TextsError
from helpers import registration_user_full_data


class TestRegisterUser:

    @allure.title(f'Проверка успешной регистрации пользователя')
    def test_register_user_get_status_200_and_get_success_true(self):
        registration_data = registration_user_full_data()
        response = requests.post(Url.url_create_user, data=registration_data)
        r = response.json()
        token_full_string = r["accessToken"]
        token = token_full_string.split()[1]
        requests.delete(Url.url_delete_user, headers={'Authorization': f'Bearer {token}'})

        assert response.status_code == 200 and r["success"] == True

    @allure.title(f'Проверка регистрации пользователя, который уже существует')
    def test_register_user_user_exist_403_text_user_already_exist(self):
        registration_data = registration_user_full_data()
        r_text_success = requests.post(Url.url_create_user, data=registration_data)
        r_text_error = requests.post(Url.url_create_user, data=registration_data)
        r_success = r_text_success.json()
        r_error = r_text_error.json()
        token_full_string = r_success["accessToken"]
        token = token_full_string.split()[1]
        requests.delete(Url.url_delete_user, headers={'Authorization': f'Bearer {token}'})

        assert r_text_error.status_code == 403 and r_error["message"] == TextsError.user_already_exist

    @pytest.mark.parametrize(
        'field, value',
        [
            ("email", ""),
            ("password", ""),
            ("name", "")
        ]
    )
    @allure.title(f'Проверка регистрации пользователя с незаполненными данными')
    def test_register_user_empty_data_get_status_403_text_required_fields(self, field, value):
        registration_data = registration_user_full_data()
        registration_data[field] = value
        response = requests.post(Url.url_create_user, data=registration_data)
        r = response.json()

        assert response.status_code == 403 and r["message"] == TextsError.not_full_data_for_registration

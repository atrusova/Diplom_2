import pytest
import requests
import allure
import json
from data import Url, TextsError
from conftest import logged_in_user
from helpers import new_user_data


class TestChangeUserData:

    @allure.title(f'Проверка изменение данных пользователя с авторизацией')
    def test_change_user_data_success_login_status_200_success_true(self, logged_in_user):
        response_user_change = requests.patch(Url.url_change_user_data,
                                              headers={'Authorization': f'Bearer {logged_in_user}'},
                                              json=new_user_data())
        r_user_change = response_user_change.json()

        assert response_user_change.status_code == 200 and r_user_change["success"] == True

    @allure.title(f'Проверка попытки изменения данных пользователя без авторизации')
    def test_get_user_data_without_login_status_401_message_should_be_authorised(self):
        response_user_change = requests.patch(Url.url_change_user_data, json=new_user_data())
        r = response_user_change.json()

        assert response_user_change.status_code == 401 and r["message"] == TextsError.actions_without_auth

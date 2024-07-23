import pytest
import requests
import allure
import json
from data import Url, TextsError
from conftest import logged_in_user


class TestGetOrders:

    def test_get_orders_auth_user_status_200_test_success_true(self, logged_in_user):
        response = requests.get(Url.url_get_user_order, headers={'Authorization': f'Bearer {logged_in_user}'})
        r = response.json()

        assert response.status_code == 200 and r['success'] == True

    def test_get_orders_without_auth_user_status_401_message_should_be_authorised(self):
        response = requests.get(Url.url_get_user_order)
        r = response.json()

        assert response.status_code == 401 and r['message'] == TextsError.actions_without_auth

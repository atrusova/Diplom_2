import pytest
import requests
import allure
import json
from conftest import logged_in_user
from data import Url, TextsError, OrderData


class TestCreateOrder:

    @allure.title(f'Проверка создания заказа с авторизацией, с указанием ингридиентов')
    def test_create_order_with_auth_status_200_success_message(self, logged_in_user):
        r_order = requests.post(Url.url_create_order,
                                headers={'Authorization': f'Bearer {logged_in_user}'},
                                data=OrderData.order_data_with_ingredients)
        r = r_order.json()

        assert r_order.status_code == 200 and r['success'] == True

    @allure.title(f'Проверка создания заказа без авторизации')
    def test_create_order_incorrect_hash_status_403_message_invalid_token(self):
        r_order = requests.post(Url.url_create_order,
                                headers={'Authorization': f'Bearer {OrderData.invalid_token}'},
                                data=OrderData.order_data_with_ingredients)
        r = r_order.json()

        assert r_order.status_code == 403 and r['message'] == TextsError.invalid_token

    @allure.title(f'Проверка создания заказа с авторизацией, без указания ингридиентов')
    def test_create_order_without_ingredients_auth_status_400_text_error(self, logged_in_user):
        r_order = requests.post(Url.url_create_order,
                                headers={'Authorization': f'Bearer {logged_in_user}'},
                                data=OrderData.order_data_without_ingredients)
        r = r_order.json()

        assert r_order.status_code == 400 and r['message'] == TextsError.order_without_ingredient

    @allure.title(f'Проверка создания заказа с авторизацией, с неверным хешем ингридиентов')
    def test_create_order_incorrect_id_ingredients_auth_status_500_order_number(self, logged_in_user):
        r_order = requests.post(Url.url_create_order,
                                headers={'Authorization': f'Bearer {logged_in_user}'},
                                data=OrderData.order_data_incorrect_id_ingredients)

        assert r_order.status_code == 500 and 'Internal Server Error' in r_order.text

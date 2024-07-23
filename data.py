class Url:
    url_create_user = 'https://stellarburgers.nomoreparties.site/api/auth/register' # эндпоинт регистрации пользователя
    url_login_user = 'https://stellarburgers.nomoreparties.site/api/auth/login' # эндпоинт авторизации
    url_change_user_data = 'https://stellarburgers.nomoreparties.site/api/auth/user'  # эндпоинт получения и обновления данных о пользователе
    url_create_order = 'https://stellarburgers.nomoreparties.site/api/orders' # эндпоинт создания заказа
    url_get_user_order = 'https://stellarburgers.nomoreparties.site/api/orders'  # эндпоинт получения заказов конкретного пользователя
    url_delete_user = 'https://stellarburgers.nomoreparties.site/api/auth/user' # эндпоинт удаления пользователя


class TextsError:
    user_already_exist = "User already exists"
    not_full_data_for_registration = "Email, password and name are required fields"
    incorrect_data_for_login = "email or password are incorrect"
    invalid_token = "invalid token"
    order_without_ingredient = "Ingredient ids must be provided"
    actions_without_auth = "You should be authorised"
    delete_user = "User successfully removed"


class OrderData:
    order_data_with_ingredients = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]}
    order_data_without_ingredients = {"ingredients": []}
    order_data_incorrect_id_ingredients = {"ingredients": ["61c0c5a714d1f82001bdaaa6d", "61c0c5a71d1f832001bdaaa6f"]}

    invalid_token = 'yJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY2OWQxN2ZkOWVkMjgwMDAxYjQ3M2UwZSIsImlhdCI6MTcyMTU4MDM1MywiZXhwIjoxNzIxNTgxNTUzfQ.MkXaG-QZbTKTEYMJ6DkPq-wcu-Y6n_Z5qqYmhCg75MY'

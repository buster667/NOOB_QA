# Используя API тренажер https://reqres.in/, подготовить позитивные и негативные тесты, использовать статусы и токены:
# 1. Зарегистрироваться.
# 2. Залогиниться под новым пользователем.
# 3. Удалить пользователя.

import requests
import pytest


class TestNewUser:
    """создаю нового пользователя"""
    @pytest.fixture()
    def new_user(self):
        response = requests.post("https://reqres.in/api/users", {"name": "Egor", "job": "Waiter",
                                                                 "email": "test@test.in", "password": "123"})
        return response

    def test_new_user(self, new_user):
        response = new_user
        if response.status_code == 201:
            print(f'Новый юзер был созданан {response.json()}')
        else:
            print('Попробуйте ещё раз')
        assert response.status_code == 201


class TestRegister:
    """Регистрирую пользователя"""
    @pytest.fixture()
    def register_user(self):
        response = requests.post("https://reqres.in/api/register", {"email": "george.bluth@reqres.in", "password": "123"})
        return response

    def test_register_user(self, register_user):
        response = register_user
        if response.status_code == 200:
            print(f'Пользователь был зарегестрирован {response.json()}')
        else:
            print('Попробуйте ещё раз')
        assert response.status_code == 200

    def test_user_token(self, register_user):
        """тест юзер токена"""
        response = register_user.json()
        if response["token"] == "QpwL5tke4Pnpja7X1":
            print(f'Токен юзера {response["token"]}')
        else:
            print('Попробуйте ещё раз')
        assert response["token"] == "QpwL5tke4Pnpja7X1"


class TestWrongRegister:
    """Регитсрация пользователя без пароля"""
    @pytest.fixture()
    def register(self):
        response = requests.post("https://reqres.in/api/register", {"email": "george.bluth@reqres.in"})
        return response

    def test_register(self, register):
        """Тест регистрации пользователя без пароля"""
        response = register
        if response.status_code == 200:
            print(f'Пользователь был зарегестрирован {response.json()}')
        else:
            print('Требуется ввод пароля!')
        assert response.status_code == 400


class TestRegisterUnknownUser:
    @pytest.fixture()
    def register_unknown_user(self):
        response = requests.post('https://reqres.in/api/register', {"email": "test@test.in", "password": "123"})
        return response

    def test_register_unknown_user(self, register_unknown_user):
        response = register_unknown_user
        if response.status_code == 400:
            for k, v in response.json().items():
                print(f'Ошибка: {v}')
        else:
            print('Пользователь был зарегистрирован')
        assert response.status_code == 400


class TestLogin:
    """Логин"""
    @pytest.fixture()
    def login(self):
        response = requests.post('https://reqres.in/api/login', {"email": "george.bluth@reqres.in", "password": "123"})
        return response

    def test_login(self, login):
        """Тест логина"""
        response = login
        if response.status_code == 200:
            for k, v in response.json().items():
                print(f'Логин успешен и ваш токен: {v}')
        else:
            print('Попробуйте ещё раз')
        assert response.status_code == 200


class TestWrongLogin:
    @pytest.fixture()
    def wrong_login(self):
        response = requests.post('https://reqres.in/api/login', {"email": "george.bluth@reqres.in"})
        return response

    def test_wrong_login(self, wrong_login):
        response = wrong_login
        if response.status_code == 200:
            print(f'Логин прошёл не удачно {response.json()}')
        else:
            print(f'Логин прошёл не удачно, код ошибки {response.status_code}. Вам нужно ввести пароль')
        assert response.status_code == 400


class TestDelete:
    """Удаление пользователя"""
    def test_delete(self):
        response = requests.delete('https://reqres.in/api/users/2')
        if response.status_code == 204:
            print('Пользователь был удалён')
        else:
            print('Попробуйте ещё раз')
        assert response.status_code == 204
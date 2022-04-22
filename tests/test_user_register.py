import pytest
import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from datetime import datetime
from lib.data_generator import data_generator


class TestUserRegister(BaseCase):

    def test_create_user_successfully(self):
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': data_generator.prepare_good_email()
        }

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")
        print(response.content)

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"

    def test_create_user_invalid_email(self):
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': data_generator.prepare_bad_email()
        }
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") == 'Invalid email format', f"Unexpected response content {response.content}"

    exclude_params = [{'username': 'learnqa', 'firstName': 'learnqa', 'lastName': 'learnqa',
                       'email': data_generator.prepare_good_email()},
                      {'password': '123', 'firstName': 'learnqa', 'lastName': 'learnqa',
                       'email': data_generator.prepare_good_email()},
                      {'password': '123', 'username': 'learnqa', 'lastName': 'learnqa',
                       'email': data_generator.prepare_good_email()},
                      {'password': '123', 'username': 'learnqa', 'firstName': 'learnqa',
                       'email': data_generator.prepare_good_email()},
                      {'password': '123', 'username': 'learnqa', 'firstName': 'learnqa', 'lastName': 'learnqa'}
                      ]

    @pytest.mark.parametrize('data', exclude_params)
    def test_create_user_with_exclude_params(self, data):
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            "utf-8") >= 'The following required params are missed:', f"Unexpected response content {response.content}"

    exclude_random_params = [
        data_generator.generate_random_string(1), data_generator.generate_random_string(250)
    ]

    @pytest.mark.parametrize('username', exclude_random_params, ids=['one symbol', '250 symbols'])
    def test_create_user_with_one_symbol(self, username):
        data = {
            'password': '123',
            'username': username,
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': data_generator.prepare_good_email()
        }
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        if len(username) == 1:
            Assertions.assert_code_status(response, 400)
            assert response.content.decode(
                "utf-8") == "The value of 'username' field is too short", f"Unexpected response content {response.content}"

            print('if : ' + username)
        else:
            Assertions.assert_code_status(response, 200)
            print('else : ' + username)
            Assertions.assert_json_has_key(response, "id")

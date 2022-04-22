import pytest
import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from datetime import datetime
from lib.data_generator import data_generator


class TestUserRegister(BaseCase):

    def setup(self):
        base_part = "learnqa"
        domain = "example.com"
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        self.email = f"{base_part}{random_part}@{domain}"
        self.email_without = f"{base_part}{random_part}{domain}"

    def test_create_user_successfully(self):
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': self.email
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
            'email': self.email_without
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

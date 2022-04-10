import requests


class TestMethodCookie:
    def test_method_cookie(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"

        response = requests.get(url)
        resp_cookies = response.cookies

        assert 'HomeWork' in resp_cookies, 'There is no HomeWork=hw_value in the response'

import requests


class TestMethodHeaders:
    def test_method_headers(self):
        url = "https://playground.learnqa.ru/api/homework_header"

        response = requests.get(url)
        resp_headers = response.headers
        assert 'x-secret-homework-header' in resp_headers, 'There is no x-secret-homework-header in the response'

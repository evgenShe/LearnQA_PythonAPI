import time

import requests
import json

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
response_asjson = response.json()
print(response_asjson)
token = response_asjson['token']
response_with_token = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": f"{token}"})
print(response_with_token.text)
time_wait = response_asjson['seconds']
time.sleep(time_wait)
response_with_token = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": f"{token}"})
print(response_with_token.text)

import requests
import json

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
response_asjson = response.json()
print(response_asjson)

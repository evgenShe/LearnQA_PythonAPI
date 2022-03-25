import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")

len_history = len(response.history)
url_last_redirect = response.url

print(len_history)
# 2
print(url_last_redirect)
# https://learnqa.ru/

import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")

len_history = len(response.history)
history = response.history
print("Количество редиректов:", len_history)
# print result:
# Количество редиректов: 3

for u in history:
    print("URL итоговый:", u.url)
# print result:
# URL итоговые: https://playground.learnqa.ru/api/long_redirect
# URL итоговые: https://playground.learnqa.ru/
# URL итоговые: https://learnqa.ru/

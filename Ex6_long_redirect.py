import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")
history = response.history

len_history = len(history)
print("Количество редиректов:", len_history)
# print result:
# Количество редиректов: 3

for u in history:
    print("Итоговый URL:", u.url)
# print result:
# URL итоговый: https://playground.learnqa.ru/api/long_redirect
# URL итоговый: https://playground.learnqa.ru/
# URL итоговый: https://learnqa.ru/

import time

import requests

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
response_asjson = response.json()
# print(response_asjson)
# {'token': 'wNxoTMwoDMyASOw0CNw0iMyAjM', 'seconds': 4}

token = response_asjson['token']
response_with_token = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": f"{token}"})
# print(response_with_token.text)
# {"status":"Job is NOT ready"}

response_with_token_as_json = response_with_token.json()
checkStatus = response_with_token_as_json['status']
if checkStatus != "Job is NOT ready":
    print("Status is NOT is true")

time_wait = response_asjson['seconds']
time.sleep(time_wait)
response_with_token2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job",
                                    params={"token": f"{token}"})
check_status_and_result = response_with_token2.json()
if check_status_and_result['status'] == "Job is ready" and check_status_and_result['result'] == check_status_and_result[
    'result']:
    print(check_status_and_result)
    # {'result': '42', 'status': 'Job is ready'}

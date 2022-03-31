import requests

request_var = [requests.get, requests.post, requests.put, requests.delete]
methods = ["GET", "POST", "PUT", "DELETE", "HEAD"]

# Ответ на задание 1.
for r in request_var:
    response1 = r("https://playground.learnqa.ru/ajax/api/compare_query_type")
    print(response1.request, "without method", response1, response1.text)
# print results:
# <PreparedRequest [GET]> without method <Response [200]> Wrong method provided
# <PreparedRequest [POST]> without method <Response [200]> Wrong method provided
# <PreparedRequest [PUT]> without method <Response [200]> Wrong method provided
# <PreparedRequest [DELETE]> without method <Response [200]> Wrong method provided

# Ответ на задания 2, 3, 4 в одном цикле.
for r in request_var:
    for m in methods:
        if r == requests.get:
            response = r("https://playground.learnqa.ru/ajax/api/compare_query_type",
                         params={"method": f"{m}"})
            print(f'{response.request}, params="method": "{m}".', response, response.text)
        else:
            response = r("https://playground.learnqa.ru/ajax/api/compare_query_type",
                         data={"method": f"{m}"})
            print(f'{response.request}, data="method": "{m}".', response, response.text)
# print results:
# <PreparedRequest [GET]>, params="method": "GET". <Response [200]> {"success":"!"}
# <PreparedRequest [GET]>, params="method": "POST". <Response [200]> Wrong method provided
# <PreparedRequest [GET]>, params="method": "PUT". <Response [200]> Wrong method provided
# <PreparedRequest [GET]>, params="method": "DELETE". <Response [200]> Wrong method provided
# <PreparedRequest [GET]>, params="method": "HEAD". <Response [200]> Wrong method provided
# <PreparedRequest [POST]>, data="method": "GET". <Response [200]> Wrong method provided
# <PreparedRequest [POST]>, data="method": "POST". <Response [200]> {"success":"!"}
# <PreparedRequest [POST]>, data="method": "PUT". <Response [200]> Wrong method provided
# <PreparedRequest [POST]>, data="method": "DELETE". <Response [200]> Wrong method provided
# <PreparedRequest [POST]>, data="method": "HEAD". <Response [200]> Wrong method provided
# <PreparedRequest [PUT]>, data="method": "GET". <Response [200]> Wrong method provided
# <PreparedRequest [PUT]>, data="method": "POST". <Response [200]> Wrong method provided
# <PreparedRequest [PUT]>, data="method": "PUT". <Response [200]> {"success":"!"}
# <PreparedRequest [PUT]>, data="method": "DELETE". <Response [200]> Wrong method provided
# <PreparedRequest [PUT]>, data="method": "HEAD". <Response [200]> Wrong method provided
# <PreparedRequest [DELETE]>, data="method": "GET". <Response [200]> {"success":"!"}
# <PreparedRequest [DELETE]>, data="method": "POST". <Response [200]> Wrong method provided
# <PreparedRequest [DELETE]>, data="method": "PUT". <Response [200]> Wrong method provided
# <PreparedRequest [DELETE]>, data="method": "DELETE". <Response [200]> {"success":"!"}
# <PreparedRequest [DELETE]>, data="method": "HEAD". <Response [200]> Wrong method provided

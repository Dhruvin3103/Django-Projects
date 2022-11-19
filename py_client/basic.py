import requests

endpoint = "http://127.0.0.1:8000/api/movie/apihome/"

# endpoint = "http://httpbin.org/anything"

response = requests.post(endpoint, params={'abc': 123}, json={"title": None, 'content':'posting the data',
                                                              'price':16.00})
print(response.json())
# print(response.text)

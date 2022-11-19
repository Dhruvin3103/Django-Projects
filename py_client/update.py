import requests

endpoint = "http://127.0.0.1:8000/api/movie/8/update/"

data = {
    'title': 'iron lord ',
    'content': 'iron 4 updated to iron lord ',
    'price': 290.00
}

response = requests.put(endpoint, json=data)
print(response.json())

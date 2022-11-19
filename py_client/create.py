import requests

endpoint = "http://127.0.0.1:8000/api/movie/"

data = {
    'title': 'iron man 5 ',
    'content': 'pehle 4 to anne do ',
    'price': 2800.00
}
response = requests.post(endpoint, json=data)
print(response.json())

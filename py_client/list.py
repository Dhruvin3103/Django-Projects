import requests

endpoint = "http://127.0.0.1:8000/api/movie/"

data = {
    'title': 'hum kabhi hero the',
    'content': 'it has 10.0 rating',
    'price': 180.00
}
response = requests.get(endpoint)
print(response.json())

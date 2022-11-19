import requests

endpoint = "http://127.0.0.1:8000/api/movie/1/"


response = requests.get(endpoint)
print(response.json())

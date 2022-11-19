from getpass import getpass

import requests

auth_endpoint = "http://127.0.0.1:8000/api/movie/auth/"
username = input('Enter the username : ')
password = getpass()
auth_response = requests.post(auth_endpoint, json={'username': username, 'password': password})
print(auth_response.json())


if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        "Authorization": f"Token {token}"
    }
    endpoint = "http://127.0.0.1:8000/api/movie/"

    response = requests.get(endpoint,headers=headers)
    print(response.json())

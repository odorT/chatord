import requests

# url = 'http://127.0.0.1:5000/api/v1'
url = 'http://192.168.79.128:81/api/v1'

data = {"username": "rustam15", "password": "rustam"}

r = requests.post(url=f'{url}/register', json=data)

print(r.text)

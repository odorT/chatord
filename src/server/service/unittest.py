import requests

url = 'http://127.0.0.1:5000/api/v1'
data = {"username": "kamran3", "password": "kamran"}

r = requests.post(url=f'{url}/register', json=data)

print(r.text)
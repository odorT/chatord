import requests


def abort(msg='Something went wrong, exiting ...'):
    print(msg)
    exit(105)


class Connection:
    def __init__(self, server_host='localhost', server_port='80'):
        self.server_port = server_port
        self.server_host = f'http://{server_host}:{server_port}/api/v1'

        self.register_endpoint = self.server_host + '/register'
        self.user_endpoint = self.server_host + '/user'
        self.health_endpoint = self.server_host + '/actuator/health'

        self.auth_token = ''
        self.user_details = ''

        try:
            res = requests.get(self.health_endpoint)
            if res.json()['status'] == 'UP':
                print("Connection established with server.")
        except:
            abort('Could not connect to server, please check the network connection.')

    def register_user(self, username, password):
        payload = {'username': username, 'password': password}

        res = requests.post(
            url=self.register_endpoint,
            data=payload
        )

        if res.status_code == 201:
            print(f'User {username} created successfully.')
        elif res.status_code == 400:
            print(f'User {username} already exists.')
            abort()
        else:
            abort('Failed in register_user method')

    def login(self, username, password, conn_details):
        payload = {'username': username, 'password': password, 'conn_details': conn_details}

        res = requests.post(
            url=self.user_endpoint,
            data=payload
        )

        if res.status_code == 200:
            print('Login successful.')
            self.auth_token = res.json()['access_token']
        elif res.status_code == 401:
            print('Wrong username or password.')
            abort()
        else:
            abort('Failed in login method')

    def logout(self):
        headers = {'Authorization': f'Bearer {self.auth_token}'}

        res = requests.patch(
            url=self.user_endpoint,
            headers=headers
        )

        if res.status_code == 200:
            print('Logged out successfully.')
            self.auth_token = ''
        elif res.status_code == 401 or res.status_code == 422:
            print(res.text)
            abort()
        else:
            abort('Failed in logout method')

    def get_all_users(self):
        headers = {'Authorization': f'Bearer {self.auth_token}'}

        res = requests.get(
            url=self.user_endpoint,
            headers=headers
        )

        if res.status_code == 200:
            self.user_details = res.json()
        elif res.status_code == 401 or res.status_code == 422:
            print(res.text)
            abort()
        else:
            abort('Failed in get_all_users method')

        return self.user_details


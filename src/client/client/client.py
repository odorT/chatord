import requests


class Connection:
    def __init__(self, server_host='localhost', server_port='80'):
        self.server_host = server_host
        self.server_port = server_port

        try:
            


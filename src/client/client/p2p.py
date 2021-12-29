import threading
import socket
from settings import *


class ReceiveThread(threading.Thread):
    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # self.sock.setblocking(False)

    def receive(self):
        (client_sock, address) = self.sock.accept()
        while True:
            data = client_sock.recv(MTU).decode(ENCODING)
            print(f'{conn.get_user_by_conn(address)}: {data}')

    def go(self) -> None:
        self.sock.bind((self.host, self.port))
        self.sock.listen(1)
        self.receive()


class SendThread(threading.Thread):
    def __init__(self, server_host, server_port):
        super().__init__()
        self.server_host = server_host
        self.server_port = server_port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # self.sock.setblocking(False)

    def connect(self):
        self.sock.connect_ex((self.server_host, self.server_port))

    def send(self, msg: str):
        self.connect()
        self.sock.sendall(msg.encode(ENCODING))

    def close(self):
        self.sock.close()




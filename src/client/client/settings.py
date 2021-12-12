from p2p import ReceiveThread, SendThread
from connection import Connection


SERVER_HOST = '127.0.0.1'
SERVER_PORT = 3456
ENCODING = 'utf-8'
MTU = 1024

conn = Connection()

import sys
import socket
import getpass
from tendo import singleton
from _thread import start_new_thread

#Проверка на создание более одного сервера
try:
    me = singleton.SingleInstance()
except:
    sys.exit()

#Устанавливаем адрес и порт
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT2 = 8001  # Port to listen on (non-privileged ports are > 1023)

server2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 2)
server2.bind((HOST, PORT2))
server2.listen()



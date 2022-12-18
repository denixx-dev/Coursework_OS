import datetime
import sys
from tkinter import *
import socket
import getpass
from tendo import singleton
from time import gmtime, strftime
from _thread import start_new_thread
from datetime import time

import itertools

#Получаем имя компьютера и пользователя
hostname = socket.gethostname()
username = getpass.getuser()

now = datetime.datetime.now()

#Проверка на создание более одного сервера
try:
    me = singleton.SingleInstance()
except:
    sys.exit()

# server1_socket()
# create_window()

def threaded(user, window_server1):
    # Добавляем текст ожидания подключения клиента
    label1 = Label(window_server1, text="Waiting for client to connect...")
    label1.grid(column=0, row=0)

    window_server1.update()
    while True:
        # user, address = server1.accept()
        # При успешном подключении клиента посылаем ему сообщение
        user.sendto("Client connected to server 1\n"
                    f"Hostname is {hostname, now.time()}\n"
                    f"Username is {username, now.time()}\n".encode("utf-8"),
                    (HOST, PORT))
        # user.sendall(f"Hostname is {hostname}\n".encode("utf-8"))
        # user.sendall(f"Username is {username}\n".encode("utf-8"))

        # Принимаем от него сообщение
        data = user.recv(1024).decode("utf-8")

        # По принятии сообщения создаем новый текст в окне
        label2 = Label(window_server1, text=f"{data}")
        label2.grid(column=0, row=1)

        window_server1.update()

        # Принимаем координаты от клиента
        coords = user.recv(1024).decode("utf-8")
        coords = list(map(int, coords.split(" ")))
        if coords[0] == 0:
            window_server1.destroy()
            break
        # label3 = Label(window_server1, text=f"{coords}")
        # label3.grid(column=0, row=2)
        window_server1.geometry(f'400x250+{coords[0]}+{coords[1]}')

        window_server1.update()
    user.close()



#Устанавливаем адрес и порт
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 8000  # Port to listen on (non-privileged ports are > 1023)
PORT2 = 8888

# Создаем окно
window_server1 = Tk()
window_server1.title("Server 1")
window_server1.geometry('400x250')
window_server1.update()

#Выполняем прослушивание порта
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server1:
server1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 2)
server1.bind((HOST, PORT))
server1.listen()

# Добавляем текст ожидания подключения клиента
label1 = Label(window_server1, text="Waiting for client to connect...")
label1.grid(column=0, row=0)

user, address = server1.accept()

window_server1.update()
while True:
    # user, address = server1.accept()
    # При успешном подключении клиента посылаем ему сообщение
    user.sendto("Client connected to server 1\n"
                f"Hostname is {hostname,strftime('%H:%M:%S', gmtime())}\n"
                f"Username is {username,strftime('%H:%M:%S', gmtime())}\n".encode("utf-8"),
                (HOST, PORT))
    # user.sendall(f"Hostname is {hostname}\n".encode("utf-8"))
    # user.sendall(f"Username is {username}\n".encode("utf-8"))

    # Принимаем от него сообщение
    data = user.recv(1024).decode("utf-8")

    # По принятии сообщения создаем новый текст в окне
    label2 = Label(window_server1, text=f"{data}")
    label2.grid(column=0, row=1)

    window_server1.update()

    # Принимаем координаты от клиента
    coords = user.recv(1024).decode("utf-8")
    coords = list(map(int, coords.split(" ")))
    if coords[0] == 0:
        window_server1.destroy()
        break
    # label3 = Label(window_server1, text=f"{coords}")
    # label3.grid(column=0, row=2)
    try:
        window_server1.geometry(f'400x250+{coords[0]}+{coords[1]}')
        window_server1.update()
        user.sendto("Window has been moved\n".encode("utf-8"), (HOST, PORT))
    except:
        user.sendto("Error while moving window".encode("utf-8"), (HOST, PORT))



user.close()
server1.close()
# start_new_thread(threaded, (user,window_server1))
window_server1.mainloop()






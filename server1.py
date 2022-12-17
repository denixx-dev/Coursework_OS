import sys
from tkinter import *
import socket
import getpass
from tendo import singleton
import itertools

# server1_socket()
# create_window()

def window_refresh():
    pass
#Проверка на создание более одного сервера
try:
    me = singleton.SingleInstance()
except:
    sys.exit()
#Получаем имя компьютера и пользователя
hostname = socket.gethostname()
username = getpass.getuser()

#Устанавливаем адрес и порт
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 8000  # Port to listen on (non-privileged ports are > 1023)

#Создаем окно
window_server1 = Tk()
window_server1.title("Server 1")
window_server1.geometry('400x250')

window_server1.update()

#Добавляем текст ожидания подключения клиента
label1 = Label(window_server1, text ="Waiting for client to connect...")
label1.grid(column=0, row=0)

window_server1.update()

#Выполняем прослушивание порта
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server1:
    server1.bind((HOST, PORT))
    server1.listen()

    while True:
        user, address = server1.accept()

        #При успешном подключении клиента посылаем ему сообщение
        user.sendto("Client connected to server 1\n"
                     f"Hostname is {hostname}\n"
                     f"Username is {username}\n".encode("utf-8"),
                    (HOST, PORT))
        # user.sendall(f"Hostname is {hostname}\n".encode("utf-8"))
        # user.sendall(f"Username is {username}\n".encode("utf-8"))

        #Принимаем от него сообщение
        data = user.recv(1024).decode("utf-8")
        #По принятии сообщения создаем новый текст в окне
        label2 = Label(window_server1, text =f"{data}")
        label2.grid(column=0, row=1)

        window_server1.update()

        #Принимаем координаты от клиента
        coords = user.recv(1024).decode("utf-8")
        coords = list(map(int, coords.split(" ")))
        # label3 = Label(window_server1, text=f"{coords}")
        # label3.grid(column=0, row=2)
        window_server1.geometry(f'400x250+{coords[0]}+{coords[1]}')



        window_server1.update()
window_server1.mainloop()



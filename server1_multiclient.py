import datetime
import multiprocessing
import sys
from tkinter import *
import socket
import getpass
from tendo import singleton
from time import gmtime, strftime
from _thread import start_new_thread
import threading
import time
import concurrent.futures as f
from multiprocessing import Process
import itertools


FORMAT = "utf-8"
# server1_socket()
# create_window()

# def test(user):
#     hostname = socket.gethostname()
#     username = getpass.getuser()
#     while True:
#         # user, address = server1.accept()
#         # При успешном подключении клиента посылаем ему сообщение
#         user.sendall("Client connected to server 1\n"
#                      f"Hostname is {hostname}\n"
#                      f"Username is {username}\n".encode("utf-8"))
#         # user.sendall(f"Hostname is {hostname}\n".encode("utf-8"))
#         # user.sendall(f"Username is {username}\n".encode("utf-8"))
#
#         # Принимаем от него сообщение
#         data = user.recv(1024).decode("utf-8")
#         print(f"{data}")
#     user.close()



def threaded(user):
    # Получаем имя компьютера и пользователя
    hostname = socket.gethostname()
    username = getpass.getuser()

    while True:
        # Принимаем от клиента команду на вывод хоста и юзера
        command_choose = user.recv(1024).decode(FORMAT)
        if command_choose == "1":
            # user, address = server1.accept()
            # При успешном подключении клиента посылаем ему сообщение
            user.sendall("Client connected to server 1\n"
                        f"Hostname is {hostname, strftime('%H:%M:%S', gmtime())}\n"
                        f"Username is {username, strftime('%H:%M:%S', gmtime())}\n".encode("utf-8"))
            # user.sendall(f"Hostname is {hostname}\n".encode("utf-8"))
            # user.sendall(f"Username is {username}\n".encode("utf-8"))
        elif command_choose == "2":
            # Создаем окно
            window_server1 = Tk()
            window_server1.title("Server 1")
            window_server1.geometry('400x250')
            window_server1.update()

            # Добавляем текст ожидания подключения клиента
            label1 = Label(window_server1, text="Waiting for client to connect...")
            label1.grid(column=0, row=0)
            window_server1.update()

            # Принимаем от него сообщение о подключении
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
            print(f"active connections: {threading.activeCount()-1}")
            window_server1.update()
            time.sleep(4)
            window_server1.destroy()
            window_server1.mainloop()
        else:
            break
    user.close()

    return 0

def main():
    # Проверка на создание более одного сервера
    try:
        me = singleton.SingleInstance()
    except:
        sys.exit()



    #Устанавливаем адрес и порт
    HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
    PORT = 8000  # Port to listen on (non-privileged ports are > 1023)
    PORT2 = 8888



    #Выполняем прослушивание порта
    # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server1:
    server1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server1.bind((HOST, PORT))
    server1.listen()


    while True:
        user, address = server1.accept()
        # thread = threading.Thread(target=threaded, args = (user, window_server1))
        # thread.start()
        # thread = f.ThreadPoolExecutor(max_workers=2)
        # thread.submit(threaded)
        # start_new_thread(test, (user,))
        start_new_thread(threaded, (user, ))
        # multiprocessing.Process(target=threaded, args=(user, window_server1))

        # break

    return 0

if __name__ == "__main__":
    main()
    # p = Process(target = threaded, args(user, window_server1))

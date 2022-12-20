import sys
import socket
import getpass
from tendo import singleton
from _thread import start_new_thread
import threading
import psutil


def threaded(user):
    while True:
        p = psutil.Process(pid=None)
        user.sendall(f"Server 2 priority: {p.nice()}".encode("utf-8"))
    user.close()

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
    server2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server2.bind((HOST, PORT2))
    server2.listen()


    while True:
        user, address = server2.accept()
        # thread = threading.Thread(target=threaded, args = (user, window_server1))
        # thread.start()
        # thread = f.ThreadPoolExecutor(max_workers=2)
        # thread.submit(threaded)
        # start_new_thread(test, (user,))
        start_new_thread(threaded, (user, ))
        # multiprocessing.Process(target=threaded, args=(user, window_server1))

        # break
    server2.close()
    return 0

if __name__ == "__main__":
    main()
    # p = Process(target = threaded, args(user, window_server1))
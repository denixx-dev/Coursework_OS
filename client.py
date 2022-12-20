from tkinter import *
import socket
HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 8000  # The port used by the server
PORT2 = 8888
FORMAT = "utf-8"

def main():
    # window_client = Tk()
    # window_client.title("Server 1")
    # window_client.geometry('400x250')

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_choose = input("Wich server do you want to connect to: ")
    # Если выбран первый сервер
    if int(server_choose) == 1:
        port = PORT
        client.connect((HOST, port))
        while True:
            server1_choose = input("User and host name (1) or window moving (2): ")
            if server1_choose == "1":
                client.send(server1_choose.encode("utf-8"))
                data = client.recv(1024).decode("utf-8")
                print(f"{data}")
            elif server1_choose == "2":
                # client.sendto("Client connected".encode("utf-8"), (HOST, PORT))
                client.send(server1_choose.encode(FORMAT))
                client.send("Client connected".encode("utf-8"))
                coords = input("Enter coordinates to"
                               " move server's window\n")
                client.send(coords.encode("utf-8"))
            else:
                break
    # Если выбран второй сервер
    else:
        port = PORT2
        client.connect((HOST, port))
        while True:
            server2_choose = input("Server priority(1) or SQM (2): ")
            if server2_choose == "1":
                client.send(server2_choose.encode(FORMAT))
                data = client.recv(1024).decode(FORMAT)
                print(data)
            elif server2_choose == "2":
                client.send(server2_choose.encode(FORMAT))
                data = client.recv(1024).decode(FORMAT)
                print(data)
            else:
                break




    # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:

    client.close()

if __name__ == "__main__":
    main()


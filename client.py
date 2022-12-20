from tkinter import *
import socket
HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 8000  # The port used by the server
PORT2 = 8888
def main():
    # window_client = Tk()
    # window_client.title("Server 1")
    # window_client.geometry('400x250')

    server_choose = input("Wich server do you want to connect to: ")
    if int(server_choose) == 1:
        port = PORT
    else:
        port = PORT2

    # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, port))

    data = client.recv(1024)
    print(data.decode("utf-8"))
    while True:
        #client.sendto("Client connected".encode("utf-8"), (HOST, PORT))
        client.send("Client connected".encode("utf-8"))

        coords = input("Enter coordinates to"
                                     " move server's window\n")

        client.sendto(coords.encode("utf-8"), (HOST, PORT))

    client.close()

if __name__ == "__main__":
    main()


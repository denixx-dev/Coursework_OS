from tkinter import *
import socket

def create_window():
    window = Tk()
    window.title("Client")
    window.geometry('400x250')

    label1 = Label(window, text = "Hello world")

    label1.grid(column=0, row=0)

    window.mainloop()


HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 8000  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    while True:
        data = client.recv(1024)
        print(f"{data}".encode("utf-8"))
        client.sendto("Client connected".encode("utf-8"), (HOST, PORT))


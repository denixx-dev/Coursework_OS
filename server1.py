from tkinter import *
import socket

# server1_socket()
# create_window()

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 8000  # Port to listen on (non-privileged ports are > 1023)

window = Tk()
window.title("Server 1")
window.geometry('400x250')

window.update_idletasks()

label1 = Label(window, text = "Waiting for client to connect")
label1.grid(column=0, row=0)

window.update_idletasks()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server1:
    server1.bind((HOST, PORT))
    server1.listen()

    while True:
        user, address = server1.accept()

        user.send("Client connected to server 1".encode("utf-8"))
        window.mainloop()
window.mainloop()


from tkinter import *
import socket
def server1_socket():
    window = create_window()

    HOST = "127.0.0.1"
    PORT = 65432


    # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #     s.bind((HOST, PORT))
    #     s.listen()
    #     conn, addr = s.accept()
    #     with conn:
    #         label2 = Label(window, text = f"Connected by {addr}")
    #         label2.grid(column=0, row=1)
    #         while True:
    #             data = conn.recv(1024)
    #             if not data:
    #                 break
    #             conn.sendall(data)

def create_window():
    HOST = "127.0.0.1"
    PORT = 65432

    window = Tk()
    window.title("Server 1")
    window.geometry('400x250')

    label1 = Label(window, text = "Sending a message...")
    label1.grid(column=0, row=0)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            label2 = Label(window, text = f"Connected by {addr}")
            label2.grid(column=0, row=1)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)

    window.mainloop()

# server1_socket()
# create_window()

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 8888  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
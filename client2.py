import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 8000  # The port used by the server

# window_client = Tk()
# window_client.title("Server 1")
# window_client.geometry('400x250')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))

    while True:
        data = client.recv(1024)
        print(data.decode("utf-8"))

        #client.sendto("Client connected".encode("utf-8"), (HOST, PORT))
        client.sendto("Client 2 connected".encode("utf-8"), (HOST, PORT))

        coords = input("Enter coordinates to"
                                     " move server's window\n")

        client.sendto(coords.encode("utf-8"), (HOST, PORT))
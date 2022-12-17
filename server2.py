import getpass
import socket
user=getpass.getuser()
hostname = socket.gethostname()
print(hostname)
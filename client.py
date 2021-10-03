
import socket

HOST = '127.0.0.1'  
PORT = 65433

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    client.sendall(b'welcome')
    data = client.recv(1024)

print('Received', format(data))
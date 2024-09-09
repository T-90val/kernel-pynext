import socket
from settings import *

def start_client():

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        message = input("Enter message to send (type 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        client_socket.sendall(message.encode())

        data = client_socket.recv(1024)
        print(f"Response from server: {data.decode()}")

    client_socket.close()

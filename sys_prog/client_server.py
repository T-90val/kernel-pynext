import socket
from settings import *

def start_server():


    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Server started and waiting for connection...")

    conn, addr = server_socket.accept()
    print(f"Connected to {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            break

        message = data.decode()
        print(f"Received message: {message}")

        if message.lower() == 'exit':
            print("Exiting server...")
            break

        conn.sendall(data)

    conn.close()
    server_socket.close()

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

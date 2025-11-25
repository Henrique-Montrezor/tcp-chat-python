"""
Module responsible for initializing the client that connects to the server.
Autor: Henrique Montrezor
"""
import socket

# Function to initialize the client and handle communication with the server
def init_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a TCP/IP socket

    client.connect(('localhost', 5000))

    finished = False

    print("Conectado ao servidor!")
    print("Digite 'sair' para terminar a comunicação.")

    while not finished:
        client.send(input('message: ').encode('utf-8')) # Send message to server
        data = client.recv(1024).decode('utf-8').lower()
        if data == 'sair':
            finished = True
        else:
            data = client.recv(1024).decode('utf-8')
            print(f"message: {data}")
            
    client.close() 

if __name__ == '__main__':
    init_client()
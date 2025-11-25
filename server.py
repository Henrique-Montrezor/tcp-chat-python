"""
module responsible for initializing and managing a TCP server that communicates with clients.
Autor: Henrique Montrezor
"""
import socket

# Function to initialize the server and handle communication with clients
def init_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a TCP/IP socket

    server.bind(('localhost', 5000))

    server.listen(5)
    client, end = server.accept() # Wait for a client to connect

    finished = False

    print("Servidor conectado por", end)
    print("Aguardando mensagens do cliente. Digite 'sair' para terminar a comunicação.")

    while not finished: 
        data = client.recv(1024).decode('utf-8').lower() # Receive message from client
        if data == 'sair':
            finished = True
        else:
            print(f"message: {data}")
            client.send(input("message: ").encode('utf-8'))
            
    client.close()
    server.close()
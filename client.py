#client.py

import socket

ip_addr = "127.0.0.1"
port = 8000

server_connection = socket(socket.AF_INET, socket.SOCK_STREAM)
server_connection.connect((ip_address, port))
print("Client connected")

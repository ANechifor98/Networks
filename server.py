#server.py
import socket
import threading

ip_addr = "0.0.0.0"
port = 8000
print("server started")
#setup, 32bit ipv4, tcp/ip
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#give the socket an ip address and port
socket_details = (ip_addr, port)
serversocket.bind(socket_details)
serversocket.listen(100)

#store the connected devices
connected_devices = {}

#function to creat a thread
def start_client_thread(connection, address):
    th = threading.Thread(target = client_thread, args = (connection, address))
    th.start()
    connected_devices[connection]["thread"] = th

#client_thread(conn, address)

#function to handle a client connection thread
def client_thread(conn, addr):
    welcome = "Welcome to the chatroom"
    conn.send(welcome.decode())

    #if the client sends us data
    #send the data to every other client

    while True:
        try:
            message = conn.recv(1024)
            if message:
                enc_message = message.encode()
                print("<{}> {}".format(addr, enc_message))
            else:
                print("<{}> has left the chat".format(addr))
        except:
            continue

#main
#loop forever
#if there is a client waiting to connect
#make a thread for the client
#gate 1

while True:
    conn, addr = serversocket.accept()
    connected_devies[conn] = {"addr":addr}
    print("{} connected".format(addr))
    #start a thread for the client's connection
    start_client_thread(conn, addr)    
    

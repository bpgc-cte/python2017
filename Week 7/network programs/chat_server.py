import socket 
from threading import *


def send_msg(socket):
	while True:
		msg = input()
		socket.send(bytes(msg,"utf-8"))	


# creates the socket
server = socket.socket()

PORT = 1234

# bind the socket to the port. 
server.bind(('localhost',PORT))   # takes a tuple

# at most 5 connections in the queue
server.listen(5)   

print("Listening for clients to connect")

# Establish connection with client.
client, addr = server.accept()    
print('Got connection from', addr)

Thread(target=send_msg, args=(client, )).start()

msg = client.recv(1024)
print(msg.decode("utf-8"))
while msg :
	msg = client.recv(1024)
	print(msg.decode("utf-8"))

client.close()

	
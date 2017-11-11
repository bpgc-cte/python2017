from socket import *
from threading import *

def send_msg(socket):
	while True:
		msg = input()
		socket.send(bytes(msg,"utf-8"))	

PORT = 1234
client = socket()

address=("localhost", PORT)

# connect to the given address
client.connect(address)

Thread(target=send_msg, args=(client, )).start()

msg = client.recv(1024)
print(msg.decode("utf-8"))
while msg :
	msg = client.recv(1024)
	print(msg.decode("utf-8"))

client.close()

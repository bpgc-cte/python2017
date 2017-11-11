from socket import *

PORT = 1234
client = socket()

address=("localhost", PORT)

# connect to the given address
client.connect(address)

print(client.recv(1024))

client.close()

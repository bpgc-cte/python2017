import socket 


def client_handler(client_sock):
    # Do things here

    client_sock.send(b'Thank you for connecting')

    # Close the connection with the client
    client_sock.close()


# creates the socket
server = socket.socket()

PORT = 1234

# bind the socket to the port. 
server.bind(('localhost',PORT))   # takes a tuple

# at most 5 connections in the queue
server.listen(5)   

print("Listening for clients to connect")

while True:
 
    # Establish connection with client.
    client, addr = server.accept()     
    print('Got connection from', addr)
    client_handler(client)
   	
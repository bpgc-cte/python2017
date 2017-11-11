# Run two instances of this program. Bind each one to a differnt port.
from socket import *
from threading import Thread

address=None

def printMessages(socket):
    while True:
        message, addr= socket.recvfrom(1000)
        print message
        print "\nRecieved message from ",addr

a = socket(AF_INET,SOCK_DGRAM)
selfPort = int(raw_input("Enter port to bind to"))


a.bind(("",selfPort))
ip = raw_input("Enter IP Address of recipient")
port = raw_input("Enter Port Number of recipient")
Thread(target=printMessages,args=(a,)).start()

while True:
    messageToSend= raw_input("Enter message to send")
    a.sendto(messageToSend,(ip,int(port)))
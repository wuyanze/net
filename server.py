from socket import *
import threading

socket = socket(AF_INET,SOCK_STREAM)
socket.bind(('',12345))
socket.listen(20)

def read(connectionSocket):
    while True:
        data=connectionSocket.recv(1024)
        print data

def write(connectionSocket):
    while True:
        data=raw_input()
        data='user2:'+data;
        connectionSocket.send(data)

while True:
    connectionSocket,addr=socket.accept()
    td1=threading.Thread(target=read,args=(connectionSocket,))
    td2=threading.Thread(target=write,args=(connectionSocket,))
    td1.start()
    td2.start()

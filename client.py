from socket import *
import threading

socket = socket(AF_INET,SOCK_STREAM)
socket.connect(('localhost',12345))

def read():
    while True:
        data=socket.recv(1024)
        print data

def write():
    while True:
        data=raw_input()
        data='user1:'+data
        socket.send(data)


def main():
    td1=threading.Thread(target=read,args=())
    td2=threading.Thread(target=write,args=())
    td1.start()
    td2.start()

if __name__=='__main__':
    main()


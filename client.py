#!/usr/bin/env python
from socket import *
import threading
import os

socket = socket(AF_INET,SOCK_STREAM)
socket.connect(('139.129.129.186',12334))

def read():
    os.system('gnome-terminal')
    new_terminals=os.listdir('/dev/pts/')
    for i in new_terminals:
        flag = True
        for y in current_terminals:
            if i == y:
                flag = False
                break
        if flag:
            term = i
    fd = open('/dev/pts/' + term, 'wr')
    while True:
        data=socket.recv(1024)
        fd.write(str(data)+'\n')

def write():
    while True:
        data=raw_input()
        socket.send(data)


def main():
    td1=threading.Thread(target=read,args=())
    td2=threading.Thread(target=write,args=())
    td1.start()
    td2.start()

if __name__=='__main__':
    current_terminals=os.listdir('/dev/pts/')
    main()


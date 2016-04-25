# #!/usr/bin/env python
# import os,sys
# import time
# current_terminals=os.listdir('/dev/pts/')
# os.system('gnome-terminal')
# time.sleep(1)
# print current_terminals
# new_terminals=os.listdir('/dev/pts')
# for i in new_terminals:
#     flag = True
#     for y in current_terminals:
#         if i==y:
#             flag = False
#     if flag:
#         term = i
# print term
# fd=open('/dev/pts/'+term,'wr')
# fd.write("yjj sb\n")
# fd.close()

from socket import *
import threading

socket = socket(AF_INET,SOCK_STREAM)
socket.connect(('139.129.129.186',12334))

def read():
    while True:
        data=socket.recv(1024)
        print data

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
    main()
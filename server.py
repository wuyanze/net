#! /usr/bin/python
from socket import *
import time
import thread
import threading
from Queue import Queue

PORT = 12345
BUFSIZE = 1024

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', PORT))
serverSocket.listen(100)


class User:
    def __init__(self, name,connectionSocket):
        self.name = name
        self.connectionSocket = connectionSocket
    def send(self,str):
        self.connectionSocket.send(str)




class UserNameSet:
    def __init__(self):
        self.Set = set()
        self.lock = threading.Lock()
    def getUserList(self):
        s = ""
        for name in self.Set:
            s+=name
            s+=','
        return s
    def addUser(self,name,connectionSocket):
        Ret = False
        self.lock.acquire()
        if self.Set.__contains__(name) == False:
            self.Set.add(name)
            Map[name] = User(name,connectionSocket)
            Ret = True
        self.lock.release()
        return Ret
    def delUser(self,name):
        self.lock.acquire()
        self.Set.remove(name)
        Map.__delitem__(name)
        self.lock.release()
    def sendMsg(self,sndName,rcvName,sendMsg):
        self.lock.acquire()
        if self.Set.__contains__(rcvName):
            timeStr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            sendMsg = timeStr+": "+sndName+":"+sendMsg + "\n"
            Map[rcvName].send(sendMsg)
        self.lock.release()

uns = UserNameSet()
Map = {}


def tcp(connectionSocket):
    Flag = True
    name = ""
    while True:
        try:
            connectionSocket.send("enter you nickname please:\n")
            str = connectionSocket.recv(BUFSIZE)
            Ret = uns.addUser(str,connectionSocket)
            if(Ret == False):
                connectionSocket.send("sorry name confict!!!\n")
            name = str
            break
        except:
            connectionSocket.close()
            break
    if Flag == False:
        return
    while True:
        try:
            str = connectionSocket.recv(BUFSIZE)
            if len(str) < 1:
                continue
            if str.startswith("query"):
                connectionSocket.send(uns.getUserList())
            elif str.startswith("send"):
                if str.count(" ") < 2:
                    connectionSocket.send("query to show all user.  (send user msg) to send msg to user.  quit to quit\n");
                    continue
                (noUse,userName,sendMsg) = str.split(" ",2)
                uns.sendMsg(name,userName,sendMsg)
            elif str.startswith("quit"):
                uns.delUser(name)
                break
            else:
                connectionSocket.send("query to show all user.  (send user msg) to send msg to user.  quit to quit\n");
        except:
            uns.delUser(name)
            connectionSocket.close()
            break
    return




def main():
    while True:
        connectionSocket, addr = serverSocket.accept()
        td = threading.Thread(target=tcp, args=(connectionSocket,))
        td.start()



if __name__ == '__main__':
    main()
#!/usr/bin/env python
import os,sys
import time
current_terminals=os.listdir('/dev/pts/')
os.system('gnome-terminal')
time.sleep(1)
print current_terminals
new_terminals=os.listdir('/dev/pts')
for i in new_terminals:
    flag = True
    for y in current_terminals:
        if i==y:
            flag = False
    if flag:
        term = i
print term
fd=open('/dev/pts/'+term,'wr')
fd.write("yjj sb\n")
fd.close()
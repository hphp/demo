#!/usr/local/bin/python

class File:
    dis_time=0

list=[]
for i in range(5):
    v=File()
    v.dis_time = 5-i
    list.append(v)
sorted(list,key=lambda File:File.dis_time)
for i in range(5):
    print list[i].dis_time

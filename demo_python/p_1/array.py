#!/usr/local/bin/python

def new_list():
    list=[2,45]
    print list[0]
    for i in range(5):
        if i < len(list):
            list[i] = i
        else :
            list.append(i)
    for i in range(5):
        print list[i]
#new_list()

def del_list():
    list = range(10)
    print list
    del list[2]
    print list
del_list()

#!/usr/bin/python

def last_ele():
    l = [1,2,3,4,5]
    print l[-1]

def l_range():
    for i in range(1,3):
        print i

def part_list():
    a = [0,1,2,3,4,5,6,7,8,9,10,11]
    b = []
    for i in range(12/4):
        b += a[i*4:(i+1)*4]
        print b

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

def new_list_with_len():
    list = [0]*4
    print list,len(list)

def del_list():
    list = range(10)
    print list
    del list[2]
    print list
#del_list()

#part_list()
#l_range()
#new_list_with_len()
last_ele()

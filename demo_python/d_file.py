#!/usr/bin/python
import os

def read_file():
    content = "ff"
    f = open(content,'r+')
    print f
    print
    l = f.readlines()
    print l
    for ele in l:
        print ele
    f.close()
    print 'reopen'
    f = open(content,'r+')
    while True:
        line = f.readline()
        if not line:
            break
        print line
    f.close()

def check_isfile():
    filename = "../demo_python"
    print os.path.isdir(filename)

def basic():
    f = open('test','w')
    f.write('xx')
    f.write('yy')
    f.writelines('xm')
    # above is append
    f.writelines('nnn' + os.linesep)
    # append and set tail to a new line.
    f.close()

def append():
    f = open("none","a")
    f.write('xx')
    f.write('xx')
    f.close()


#append()
#check_isfile()
read_file()

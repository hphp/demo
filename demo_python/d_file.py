#!/usr/bin/python
import os

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
check_isfile()

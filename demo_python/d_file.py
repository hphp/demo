#!/usr/bin/python
import os

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


append()

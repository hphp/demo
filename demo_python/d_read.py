#!/usr/bin/python

def basic():
    content = "ff"
    f = open(content,'r+')
    s = "hello"
    f.write(s)
    print f

    print f.readlines()


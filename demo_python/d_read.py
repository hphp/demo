#!/usr/bin/python

content = "ff"
f = open(content,'r+')
s = "hello"
f.write(s)
print f

print f.readlines()


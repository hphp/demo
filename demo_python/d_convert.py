#!/usr/bin/python

def int_to_ascii():
    i = 1
    print unichr(i+ord('a'))

def int_to_str():
    i = 1
    print str(i)

def list_str_to_int():
    r = ['1','2','3']
    results = map(int , r)
    print type(results),len(results),type(results[0])

int_to_ascii()
#int_to_str()
#list_str_to_int()

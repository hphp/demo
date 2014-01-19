#!/usr/bin/python
import os
import sys

def basic():
    print len(sys.argv)
    for arg in sys.argv:
        print arg
    print sys.argv[1]
    print sys.argv[2]

basic()

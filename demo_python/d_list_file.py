
import os
import fnmatch

def basic(director):
    ll = os.listdir("./")
    ll = os.listdir("../")
    ll = os.listdir(director)
    i = 0
    for i in range(10):
        print ll[i] 

def d_filter(directory, reg):
    ll = os.listdir(directory)
    ll = fnmatch.filter(ll, reg)
    for i in range(min(10, len(ll))):
        print ll[i] 

def test_basic():
    basic("./")
    basic("./*.py")

d_filter("./","*.py")

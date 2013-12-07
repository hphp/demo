
import numpy

a = 3

def change_global():
    global a
    print a
    a = 30
    print a

def show_global():
    global a
    print a

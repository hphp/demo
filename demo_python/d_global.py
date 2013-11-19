
from d_class import d_TEMPLATE

a = 4
b = int()
c = d_TEMPLATE()

def test_class():
    global c
    print c.m
    c = d_TEMPLATE(2,3,4)
    print c.m

def test_a():
    global a, b
    print a, b
    #global a, b
    print a, b
    a += 4
    b = 4

test_class()
print c.m
#test_a()
#print a, b

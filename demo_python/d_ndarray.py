#!/usr/bin/python

import numpy

def reshape():
    a = [[14,3,3,4],[2,2,3,4],[3,23,3,3],[4,3,3,3]]
    b = numpy.asarray(a)
    print b,type(b),b.shape
    c = b.reshape(16,)
    print "co"
    print c,type(c),c.shape

def part_ndarray():
    b = numpy.asarray(a)
    print b
    print b[0:3]

def attach_ndarray():
    a = [[1,2,3,4],[2],[3],[4]]
    aa = numpy.asarray(a)
    b = []
    c = numpy.asarray(b)
    for i in range(2):
        c = numpy.concatenate((c,aa[i*2:(i+1)*2]))
    print c
    print b

#attach_ndarray()
reshape()

#!/usr/bin/python

import numpy

def to_tuple():
    a = [[14,3,3,4],[2,2,3,4],[3,23,3,3],[4,3,3,3]]
    b = numpy.asarray(a)
    print b,type(b),b.shape,b.shape[0],b.shape[1]
    c = numpy.array(b) # returns ndarray
    print c,type(c)


def connect():
    a = [[14,3,3,4],[2,2,3,4],[3,23,3,3],[4,3,3,3]]
    b = numpy.asarray(a)
    print b,type(b),b.shape,b.shape[0],b.shape[1]
    c = numpy.asarray(a)
    d = (a,b) 
    print d,type(d),d.shape,d.shape[0],d.shape[1]

def shape():
    a = [[14,3,3,4],[2,2,3,4],[3,23,3,3],[4,3,3,3]]
    b = numpy.asarray(a)
    print b,type(b),b.shape,b.shape[0],b.shape[1]

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
#reshape()
#shape()
#connect()
to_tuple()

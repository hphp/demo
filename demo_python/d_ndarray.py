#!/usr/bin/python

import numpy

def ndarray_init():
    a = numpy.arange(15) # ok
    print type(a),a.shape # <type 'numpy.ndarray'> (15,)
    a = numpy.array(15) #
    print type(a),a.shape # ndarray, ()
    a = numpy.zeros(15, dtype='float32')
    print type(a),a.shape # ndarray, (15,)
    a = numpy.zeros(15)
    print type(a),a.shape # ndarray, (15,)

def ndarray_calculation():
    b = [5,4,3,2,1,0,1,2,3,4,5,6]
    a = numpy.array(b)
    c = numpy.asarray(a,dtype='float32') / 2
    print c
    c = a/2 
    print c

def get_arg_index():
    b = [5,4,3,2,1,0,1,2,3,4,5,6]
    a = numpy.array(b)
    arg_list = numpy.argwhere(a == 2) 
    print "type," , type(arg_list)
    print "list,", arg_list # [[3] \n [7]]
    print "len,",len(arg_list)
    print "shape,", arg_list.shape

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
    d = (a,b) # not a way to connect two arrays.
    print d,type(d) # tuple
    d = numpy.concatenate((b,c)) # good way to connect two ndarray
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
connect()
#to_tuple()
#get_arg_index()
#ndarray_calculation()
#ndarray_init()

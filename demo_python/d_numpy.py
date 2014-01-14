
import numpy
import random

def f_ones():
    l = numpy.ones(2)
    print l # [ 1. 1. ]
    m = numpy.ones(l)
    print m # [ [ 1. ] ]
    l = numpy.ones((3,4))
    print l
    m = numpy.ones(l.shape)
    print m
    m = numpy.ones(l)
    print m

def f_dtype():
    l = numpy.arange(10)
    print l.dtype

def f_amax():
    l = numpy.arange(10)
    print numpy.amax(l)

def f_arange():
    x = numpy.arange(9.).reshape(3,3)
    print x
    x = numpy.arange(9).reshape(3,3)
    print x
    print numpy.arange(400)[:,numpy.newaxis]

def f_where():
    # where( condition ) , return position that satisfy condition
    l = numpy.arange(10)
    l2 = numpy.where((l>3)&(l<7))
    print l2 # [ 4,5,6 ]
    l3 = (l>3)&(l<7)
    print l3 # [ False,....True,True, .. False ]
    l4 = numpy.where(l3)
    print l4 # [ 4,5,6 ]

    # prove that it returns the postion instead of the element value
    l = numpy.arange(10,20)
    l2 = numpy.where((l>13)&(l<17))
    print l2 # [ 4,5,6 ]
    l3 = (l>13)&(l<17)
    print l3 # [ False,....True,True, .. False ]
    l4 = numpy.where(l3)
    print l4 # [ 4,5,6 ]
    #uni_l = rng.uniform(0, 255, size=(2500,))

    #
    x = numpy.arange(10,19).reshape(3,3)
    y = numpy.arange(10,25)
    z = numpy.arange(10,12)
    m = numpy.arange(10,19)
    fx = numpy.arange(10.,19.).reshape(3,3)
    print x
    print numpy.where( x > 15 )
    print numpy.where( x > 13 )
    print numpy.where( x>15, x, -1 )
    #print numpy.where( x>15, y, -1 ) # different size --> shape mismatch
    #print numpy.where( x>15, z, -1 ) # different size
    #print numpy.where( x>15, m, -1 ) # shape mismatch
    print "float vs integer" , numpy.where( fx > 12. , x, -1)
    print "float vs integer" , numpy.where( fx, x, -1)

    x = numpy.arange(10,22).reshape(3,4)
    print x
    print numpy.where( x > 15 )
    print numpy.where( x > 13 )

def uniform():
    rng = numpy.random.RandomState(23555)
    uni_l = rng.uniform(0, 255, size=(2500,))
    print type(uni_l)
    l = numpy.asarray(uni_l, dtype='int32')
    print type(l), l.shape
    rl = random.sample(l, 10)
    print rl

def basic():
    a = 55.7
    b = numpy.float64(a)
    print type(b),b
    c = numpy.float32(b)
    print type(c),c

    if (c >= 0.) & (c < 100.):
        print 'c between[0,100)'

    s = 0
    e = 100
    if (c >= s ) & (c < e):
        print 'c between [ %d, %d )' % (s,e)

#basic()
#uniform()
f_arange()
#f_amax()
#f_dtype()
#f_where()
#f_ones()

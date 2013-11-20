
import numpy
import random

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
uniform()

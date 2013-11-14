
import numpy
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

from numpy import arange
def if_in_range():
    if 5 in range(0,10):
        print 'good'
    if 5.5 in range(0,19):
        print '5.5 in range(0,19)' # not good

def judge():
    if (5.5 >= 0.) & (5.5 < 19.):
        print '5.5 between(0,19)'
    if 5.5 >= 0. & 5.5 < 19.: # not good
        print '5.5 between(0,19)'

def range_step():
    for i in range(1, 10, 5):
        print i
    for i in arange(1., 2, 0.5):
        print i

def range_from_not_0():
    for i in range(2, 10, 5):
        print i
#range_step()
range_from_not_0()

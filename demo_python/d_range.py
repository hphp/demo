
if 5 in range(0,10):
    print 'good'
if 5.5 in range(0,19):
    print '5.5 in range(0,19)' # not good

if (5.5 >= 0.) & (5.5 < 19.):
    print '5.5 between(0,19)'
if 5.5 >= 0. & 5.5 < 19.: # not good
    print '5.5 between(0,19)'

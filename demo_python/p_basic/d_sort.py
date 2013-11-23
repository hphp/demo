#!/usr/bin/python

import operator
x = {1: 2, 3: 4, 4:3, 2:1, 0:0}
print x
sorted_x = sorted(x.iteritems(), key=operator.itemgetter(0))
print sorted_x
sorted_x = sorted(x.iteritems(), key=operator.itemgetter(1))
print sorted_x

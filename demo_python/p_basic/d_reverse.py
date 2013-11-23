#!/usr/bin/python

n_list = [9,5,8,7,6]

print n_list
print reversed(n_list)

import operator

n_dict = {}
n_dict[0] = "9"
n_dict[1] = "5"
n_dict[2] = "7"
n_dict[3] = "6"

print n_dict
o_list = sorted(n_dict.iteritems(),key = operator.itemgetter(1), reverse=True)
print o_list
o_list = sorted(n_dict.iteritems(),key = operator.itemgetter(1))
print o_list
print o_list[0]
print o_list[0]
print o_list[0][0]
print o_list[0][1]
print o_list[1]

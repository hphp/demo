#!/usr/bin/python

def basic() :
	tmp_dict = {}
	# key: 'a'   value: {}
	print tmp_dict
	t = tmp_dict.setdefault('a', {})
	t['x']=344
	print tmp_dict
	tmp_dict[2] = [5,6,6] 

	print tmp_dict
	tmp_dict[1]='abc'
	print tmp_dict
	tmp_dict.setdefault(1, 2)
	print tmp_dict

#basic()

def dim_2_basic():
	print
	print "2 dimension dict basic"
	c_dict = {}
	c_dict['x'] = {}
	c_dict['x'][0] = 1
	c_dict['x'][1] = 1
	c_dict['x'][2] = 1
	c_dict['y'] = {}
	c_dict['y'][4] = 2
	c_dict['y'][9] = 2
	c_dict['y'][3] = 2
	print c_dict

#dim_2_basic()

def dict_remove():
	print "this is the dict_remove function"
	c_dict = {}
	c_dict['x'] = 'b'
	c_dict['y'] = 'c'
	print "current dict : "
	print c_dict
	del(c_dict['y'])
	print "after deleting"
	print c_dict

#dict_remove()

def dict_2dim_remove():
	print
	print "dim 2 dict to remove"
	c_dict = {}
	c_dict['x'] = {}
	c_dict['x'][0] = 1
	c_dict['x'][1] = 1
	c_dict['x'][2] = 1
	c_dict['y'] = {}
	c_dict['y'][4] = 2
	c_dict['y'][9] = 2
	c_dict['y'][3] = 2
	print "basic dict"
	print c_dict

	del(c_dict['x'][0])
	print "after del [x][1]"
	print c_dict
	del(c_dict['x'])
	print "after del [x]"
	print c_dict

#dict_2dim_remove()

# easy demo

ed_dict = {}
#ed_dict[10] = "x"
ed_dict["xx"] = 10
#find by key .
if 10 not in ed_dict :
	ed_dict[10] = "xxx"
ed_dict[10] += "yy"
print ed_dict

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
print o_list[0][0]
print o_list[0][1]
print o_list[1]

#!/bin/python

from urllib import urlencode
import urllib

#m = {'name':'peter','gender':'fe'}
m = '/\good'
#print urlencode(m)
print urllib.quote(m)

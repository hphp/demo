#!/bin/python
#encoding:utf-8  

from urllib import urlencode
import urllib

def d_urlencode():
    #m = {'name':'peter','gender':'fe'}
    m = '/\good'
    #print urlencode(m)
    print urllib.quote(m)

def d_zhongwen_encoding():
    #please see as encoding:utf-8
    print "hello morto 你好！大魔tua！～"

#d_zhongwen_encoding()

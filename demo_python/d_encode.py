#!/bin/python
#encoding:utf-8  

from urllib import urlencode
import urllib

def d_urlencode():
    #m = {'name':'peter','gender':'fe'}
    m = '/\good'
    #print urlencode(m)
    print urllib.quote(m)

def unicode_basic():
    strr = u'你好，大世界'
    print unicode('aaa')
    print type(unicode('aaa'))
    print unicode(strr)
    print type(unicode(strr))
    unicode_str = unicode(strr)
    print unicode_str.encode('utf-8'), type(unicode_str.encode('utf-8'))
    #print unicode('你好 小童通')

def d_zhongwen_encoding():
    #please see as encoding:utf-8
    print "hello morto 你好！大魔tua！～"
    strr = u'你好，大世界'
    strr
    print strr
    utf8_encode = strr.encode('utf-8')
    print utf8_encode

def unicode_utf8():
    msg = "你好，大卡～"
    json_obj = {}
    json_obj['hua'] = msg
    mmm = json_obj['hua']
#    json_obj['hua'].decode('utf-8')
    print msg
    print json_obj
    print json_obj['hua']
    print mmm
#d_zhongwen_encoding()
#unicode_utf8()
unicode_basic()

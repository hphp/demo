#!/usr/bin/python
# -*- coding: utf-8 -*-

import string
import chars

def ischinese(uchar):
    """判断一个unicode是否是汉字"""
    if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
        return True
    else:
        return False

def isAscii(uchar):
    if uchar in chars.ascii:
        return True

def filter_ch():
    import d_text
    text = d_text.read_text("d_file.ch.in", normalize=0)
    l = ""
    for line in text:
        for ch in line:
            if isAscii(ch):
                l += ch
    d_text.write_text("tmp", l, normalize=0)
    f = open("tmp", "r")
    wf = open("t", "a")
    lines = f.readlines()
    f.close()
    for line in lines:
        if line != "\n":
            wf.write(line) 
    wf.close()

def f_trans():
    aTob = string.maketrans('e','b')
    print type(aTob) 
    s = 'hello world'
    print s.translate(aTob)
    print s.translate(aTob, 'o')

def ascii_():
    print ord('!')
    print ord('~')
    print chr(0)
    print chr(255)
    print ord(' ')

def space_ascii():
    a = ' '
    print "%d" % ord(a)
    x = (a >= '!' and a <= '~')
    print x
    x = (ord(a) >= ord('!') and ord(a) <= ord('~'))
    print x

def ascii_to_char():
    new_char = "%c"%2
    print new_char
    new_char = "%c"%182
    print new_char
    new_char = "%c"%33
    print new_char
    new_char = "%c"%174
    print new_char

def basic():
    a = "abcd"
    b = "0123"
    c = "!@#$"

    sep = "."
    print sep.join((a,b,c)) #a.b.c
    print sep.join([a,b,c]) #a.b.c 
    print " ".join([a,b,c])
    # print " ".join(a,b,c) no valid

def strange():
    ns = "hellomorto-%08d!!"%(3+1)
    print ns

def rep():
    ostr = "hello world i love u "
    # nstr = ostr.replace(" ",some-special-char)  could not right now , encodes or sth
    new_char = "%c"%216
    nstr = ostr.replace(" ",new_char)
    print ostr, nstr

def str_join():
    a = "a"
    b = "b"
    c = "c"
    print a+b+c

def str_format():
    s = "good,{0}".format("morning")
    print s
    s = "good,{0}".format("13423432")
    print s
    s = "good,{0}".format("342.5")
    print s
    #s = "{'good':{0}}".format("342.5") # cant work
    #print s

def str_pos():
    s = "gooood"
    print s[0:-1]

def str_equal():
#    print "sdfs".equals("sdfs") # no equals function
    print "sdfs" == "sdfs"
    print "sdfs" == "sdfs" and True
    print "sdfs" == "sdfs" and not True
    print "sdfs" == "sdfs" and False

#basic()
#strange()
#rep()
#ascii_to_char()
#space_ascii()
#ascii_()
#f_trans()
#filter_ch()
#str_join()
#str_format()
#str_pos()
str_equal()

#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import codecs

def read_chinese():
    content = "d_file.ch.in"
    ###### cant read, because each element in line is a ascii ###########
    #f = open(content,'r+')
    #for i in range(10):
    #    line = f.readline()
    #    if not line:
    #        break
    #    eng_line = ""
    #    for ele in line:
#   #         print ord(ele)
    #        if ele >= chr(0) and (ele) <= chr(225):
    #            eng_line += ele
    #    print 'thisiseng-'+eng_line, '--------thisisch:', line
    #f.close()
    ###### cant read, because each element in line is a ascii ###########
    ########## codecs read ###############
    with codecs.open(content, "r", "utf-8") as stream:
        result = stream.read()
    

    for i,basic_letter in enumerate(result):
        print basic_letter
        if i > 20:
            break

def rename():
    os.system("touch temp")
    os.rename("temp", "temp2")
    f = open("temp2", "r")
    f.close()
    print "temp2 exists"
    f = open("temp", "r")
    f.close()

def read_file():
    content = "d_file.in"
    f = open(content,'r+')
    print f
    print
    l = f.readlines()
    print l
    for ele in l:
        print ele
    f.close()
    print 'reopen'
    f = open(content,'r+')
    while True:
        line = f.readline()
        if not line:
            break
        print line
    f.close()
    print 'reopen'
    f = open(content,'r+')
    while True:
        line = f.readline()
        if not line:
            break
        first_part = line.split("\n")[0]
        stuff, price = first_part.split(",")
        print stuff
        print price
    f.close()

def check_isfile():
    filename = "../demo_python"
    print os.path.isdir(filename)

def basic():
    f = open('test','w')
    f.write('xx')
    f.write('yy')
    f.writelines('xm')
    # above is append
    f.writelines('nnn' + os.linesep)
    # append and set tail to a new line.
    f.close()

def append():
    f = open("none","a")
    f.write('xx')
    f.write('xx')
    f.close()


#append()
#check_isfile()
#read_file()
#rename()
read_chinese()

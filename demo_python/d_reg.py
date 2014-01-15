# regularize - 
import re

def get_digit():
    pattern = re.compile(u'\d*')
    match = pattern.match('12345hello67890')
    print match.group()

def match():
    pattern = re.compile(u'\d*')
    match = pattern.match('12345hello67890')
    print match.group()

def findall():
    pattern_d = re.compile(u'\d+') # digit
    pattern_w = re.compile(u'\w+') # word
    f_d_list = pattern_d.findall('12345hello67890')
    f_w_list = pattern_w.findall('12345hello67890')
    print f_d_list # [ '12345' , '67890' ]
    print f_w_list # [ '12345hello67890' ]

#get_digit()
#match()
#findall()

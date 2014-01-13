
import string

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

def strange():
    ns = "hellomorto-%08d!!"%(3+1)
    print ns

def rep():
    ostr = "hello world i love u "
    # nstr = ostr.replace(" ",some-special-char)  could not right now , encodes or sth
    new_char = "%c"%216
    nstr = ostr.replace(" ",new_char)
    print ostr, nstr


#strange()
#rep()
#ascii_to_char()
#space_ascii()
#ascii_()
f_trans()

#!/usr/bin/python
import os
import cgitb
import cgi

print "Content-type:text/html\r\n\r\n"
#cgitb.enable()
form = cgi.FieldStorage()
if "xx" not in form : 
    print "xx"
else : 
    print form["xx"].value
    f.open('tempx','w')
    f.write(form["xx"].value)
if "xx3" not in form : 
    print "xx3"
else : 
    print form["xx3"].value
    f.open('tempx','w')
    f.write(form["xx3"].value)

print '--------------'
print form.getvalue('xx3')
print form.getvalue('xx')


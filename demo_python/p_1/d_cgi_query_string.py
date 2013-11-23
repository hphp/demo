#!/usr/bin/python
import os
import cgitb
import cgi
import json
#import datetime

print "Content-type:text/html\r\n\r\n"

print 'good'
#ans = os.environ["HOME"]
#print ans
def get_ticket():
    ticket = 'none'
    if "QUERY_STRING" in os.environ : 
        query_str = os.environ["QUERY_STRING"]
        print query_str
        print query_str[7:len(query_str)]
        ticket = query_str[7:len(query_str)]
for param in os.environ.keys():
    print param + 'pa'
    print os.environ[param] + 'x'
#cgi.print_environ()
'''
form = cgi.MiniFieldStorage()
if "ticket" in form:
    print 'hi' + ticket
ans = os.environ["QUERY_STRING"]
print ans
'''
ticket = get_ticket()
print format(ticket)
print len(format(ticket))

#!/usr/local/bin/python

import httplib

con = httplib.HTTPConnection("172.27.208.76")
con.request("HEAD","http://172.27.208.76/ip_distribution/xxx.html")
ans = con.getresponse()
print ans.msg
print ans.msg["etag"]


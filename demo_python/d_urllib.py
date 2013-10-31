#!/usr/local/bin/python
import urllib2

def get_header_test():
    url  = "http://172.27.208.76/ip_distribution/home.html"
    f = urllib2.urlopen(url)
    #this method mayget the whole url , when 
    msg = f.info()
    for i in enumerate(msg):
        print i
    print '---'
    print msg["etag"] # this works
    print msg
    print '---'
    print len(msg)
    print '---'
    print msg.getplist() # dont know what it is
    print '---'
    print msg.getparam("ETag") # dontknow what it is
    print '---'

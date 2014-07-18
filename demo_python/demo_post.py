import sys, urllib2, urllib

url = "http://www.baidu.com"
data = '{"sdfsdfsdfsdf":22}'

req = urllib2.Request(url)
fd = urllib2.urlopen(req, data)
while 1:
    data = fd.read(1024)
    if not len(data):
        break
    #sys.stdout.write(data) # its ok
    print data

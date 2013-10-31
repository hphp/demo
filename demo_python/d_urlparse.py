#!/usr/local/bin/python

import urlparse

def test_for_basic_urlparse():
    url="http://172.27.208.76/ip_distribution/home.html"
    parse = urlparse.urlparse(url)
    print parse.netloc

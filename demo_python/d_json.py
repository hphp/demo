#!/usr/bin/python

import json

def basic():
    #s = "{'b':2}"
    s = "[{\"a\": \"A\", \"c\": 3.0, \"b\": [2, 4]}]"
    #,{'b':3}]"
    #s = "aa"
    #ss = unicode(s)
    #a = json.dumps(s)
    b = json.loads(s)
    print b
    print len(b)
    print b[0]["a"]
    for o in b:
        print o["a"]


def json_dump():
    json_value = {'a':'b',1:2}
    print json_value
    json_obj = json.dumps(json_value)
    print json_obj

def get_key_value():
    json_obj = {'a':2, '1':'3', '2': 4}
    for key in json_obj.keys():
        print key
    ss = ""
    for key in json_obj.keys():
        ss += key
    print ss

#basic()
#json_dump()
get_key_value()

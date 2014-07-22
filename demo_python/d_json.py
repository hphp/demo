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

def iterate_json_obj():
    s = '{"a": "A", "c": 3.0, "b": [2, 4], "dd":{"aacc":"aacc","bb":"bb","c":3}}'
    #s = '[{"a": "A", "c": 3.0, "b": [2, 4]}]' # list
    obj_s = json.loads(s)
    print obj_s.keys()
    for key in obj_s.keys():
        print key, " ", obj_s[key], type(obj_s[key])
        if type(obj_s[key]) == type(dict):
            for s_key in obj_s[key]:
                print s_key, obj_s[key][s_key], type(obj_s[key][s_key])

#
def iterate_json_obj_several_jsobj():
    s = '[{"a": "A"}, {"c": 3.0}, {"b": [2, 4]}, {"dd":{"aacc":"aacc","bb":"bb","c":3}}]'
    #s = '[{"a": "A", "c": 3.0, "b": [2, 4]}]' # list
    obj_s = json.loads(s)
    for element in obj_s:
        print element, type(element)
        if type(element) == type(dict):
            for s_key in element: 
                print s_key, element[s_key]

# load obj to json formatted 
def json_dumps():
    json_obj = {'a':'b',1:2}
    print json_obj, type(json_obj)
    json_str = json.dumps(json_obj)
    print json_str, type(json_str)

# load json formatted str to obj
def json_loads():
    #json_str = "{'a':'b','1':2}" # cant work
    json_str = '{"a": "b", "1": 2}' # fit format
    print json_str # str
    json_obj = json.loads(json_str) 
    print json_obj, type(json_obj)

def get_key_value():
    json_obj = {'a':2, '1':'3', '2': 4}
    for key in json_obj.keys():
        print key
    ss = ""
    for key in json_obj.keys():
        ss += key
    print ss

def read_from_file():
    filehandle = open('d_json.in')
    load = json.load(filehandle)
    print load
    filehandle.close()
#basic()
#json_dumps() # from obj to str
#json_loads() # from str to obj
#get_key_value()
#read_from_file()
#iterate_json_obj() # iterate json object using keys.
iterate_json_obj_several_jsobj()

#!/usr/bin/python
import json

data = [ { 'a':'A', 'b':(2, 4), 'c':3.0 } ]
data_string = json.dumps(data)
print 'ENCODED:', data_string
decoded = json.loads(data_string)
print 'DECODED:', decoded
print 'ORIGINAL:', type(data[0]['b'])
print 'DECODED :', type(decoded[0]['b'])

'''
ENCODED: [{"a": "A", "c": 3.0, "b": [2, 4]}]
DECODED: [{u'a': u'A', u'c': 3.0, u'b': [2, 4]}]
ORIGINAL: <type 'tuple'>
DECODED : <type 'list'>
'''

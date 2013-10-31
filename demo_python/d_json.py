#!/usr/bin/python

import json

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

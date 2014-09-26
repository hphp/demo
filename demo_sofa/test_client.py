#!/usr/bin/env python
#
import sys
import json
import httplib
import contextlib
import urlparse
import base64
import string

def main():
    if len(sys.argv) != 2:
        print >>sys.stderr, 'usage: %s address' % sys.argv[0]
        sys.exit(-1)
    
    address = urlparse.urlparse(sys.argv[1]);

    req = json.dumps({
        'jsonrpc': '2.0',
        'method': 'Deploy',
        'params': [{
            'prodID': '111',
            'prodName': 'xunren',
            'strategy': 'face',
            'environment': 'test',
            'jsonMachineInfo' : '{123}'
            }],
        'id': 12345
    })
    headers = {
        'Content-Length': str(len(req)),
        'Accept': 'text/plain'
    }
    with contextlib.closing(httplib.HTTPConnection(address.netloc)) as c:
        c.request('POST', address.path, req, headers)
        #resp = json.loads(c.getresponse().read())
        print '%s' %c.getresponse().read()
        #if 'error' not in resp:
        #    print '%s' % json.dumps(resp)
        #else:
        #print 'jsonRet: %s' % resp['result']['_ret']['jsonRet']

if __name__ == '__main__':
    main()


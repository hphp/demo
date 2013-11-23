#!/usr/local/bin/python

import _mysql
import sys

con = None

try : 
    con = _mysql.connect('localhost','root','','ip_distribution');
    con.query("select * from pro_pro_dis");
    result = con.use_result()
    print result
    while True:
        rows = result.fetch_row()
        if not rows : 
            break
        print rows

    con.query("select * from pro_pro_dis");
    result = con.use_result()
    v = []
    while True:
        rows = result.fetch_row()
        if not rows : 
            break
        v.append(rows[0])

    for i in enumerate(v):
        print i[0]
        print i[1]
        print i[1][0]
        #print i[2]



except _mysql.Error, e :
    print "Error %d: %s" % (e.args[0] , e.args[1])
    sys.exit(1)

finally:
    if con:
        con.close()

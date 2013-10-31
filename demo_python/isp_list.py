#!/usr/local/bin/python
import os
import cgitb
import cgi
import json
import _mysql
#import datetime

def get_query_v(query):

    con = None

    try : 
        con = _mysql.connect('localhost','root','','ip_distribution');
        con.query(query);
        #"select * from pro_pro_dis");
        result = con.use_result()
        #print result
        v = []
        while True:
            rows = result.fetch_row()
            if not rows : 
                break
            #print rows[0]
            v.append(rows[0])

        for i in enumerate(v):
            a = 2
            #print i[1][0]
            #print i[1][1]
            #print i[0]
            #print i[1]
            #return i[1][0]
            #print i[2]
        return v 

    except _mysql.Error, e :
        print "Error %d: %s" % (e.args[0] , e.args[1])
        sys.exit(1)

    finally:
        if con:
            con.close()


print "Content-type:text/html;charset=gb2312;\r\n\r\n"

query = "select distinct isp_id,isp_name from isp_info"

isp_list = get_query_v(query)
s = '{"page":1,"records":'
s += format(len(isp_list))
s += ',"rows":['
flag = 0;
for i in enumerate(isp_list):
    if flag > 0 : 
        s += ','
    s += '{"id":';
    s += format(flag)
    flag += 1
    s += ','
    s += '"cell":['
    s += format(i[1][0])
    s += ','
    s += '"'
    s += i[1][1]
    s += '"'
    s += ']'
    s += '}'

s += ']}'

print s

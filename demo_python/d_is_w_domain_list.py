#!/usr/local/bin/python
import os
import cgitb
import cgi
import json
import _mysql
#import datetime

def get_version():
    query_str = "none"
    #if 1 :
    if "QUERY_STRING" in os.environ : 
        query_str = os.environ["QUERY_STRING"]
        #query_str = "version=2368&_search=false&nd=1343965989577&rows=20&page=1&sidx=&sord=asc"
        #print query_str + 'nice'
        list = query_str.split('&')
        for part in list:
            #print part
            if part[0:8] == 'version=' :
                return part[8:len(part)]
    return query_str 

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


print "Content-type:text/html\r\n\r\n"

version = get_version()
if version == 'none':
    print ''
else :
    query = "select distinct c.b_id,bi.b_domain from configure c , bussiness_info bi where c.version= %s and c.b_id = bi.b_id " % (version)

    list = get_query_v(query)
    s = '{"page":1,"records":1,"rows":['
    flag = 0;
    for i in enumerate(list):
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

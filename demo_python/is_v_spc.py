#!/usr/local/bin/python
import os
import cgitb
import cgi
import json
import _mysql
#import datetime

print "Content-type:text/html;charset=gb2312;\r\n\r\n"


def get_query_str(query_name):
    query_value = "none"
    query_value = "2358"
    if "QUERY_STRING" in os.environ : 
        query_str = os.environ["QUERY_STRING"]
        list = query_str.split('&')
        for listi in list:
            if listi[0:len(query_name)] == query_name:
                query_value = listi[len(query_name)+1:len(listi)]

    return query_value 
def get_query(query):

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
            v.append(rows[0])

        for i in enumerate(v):
            #print i[0]
            #print i[1]
            return i[1][0]
            #print i[2]
        return None

    except _mysql.Error, e :
        print "Error %d: %s" % (e.args[0] , e.args[1])
        sys.exit(1)

    finally:
        if con:
            con.close()

def get_query_r(query):

    con = None

    try : 
        con = _mysql.connect('localhost','root','','ip_distribution');
        con.query(query);
        result = con.use_result()
        v = []
        while True:
            rows = result.fetch_row()
            if not rows : 
                break
            for ele in rows:
                #print ele
                v.append(ele)

        return v

    except _mysql.Error, e :
        print "Error %d: %s" % (e.args[0] , e.args[1])
        sys.exit(1)

    finally:
        if con:
            con.close()
version = (get_query_str("version"))
#print (version)
query = "select operator , date , last_seconds, time, comment, status ,log_v ,status_c from ipd_conf_log where version = %s " % (version)
v = get_query_r(query)
'''
for i in v:
    for j in i:
        print j
        '''
#print len(v) 
operator = 'unkown'
date = 'unknow'
last_seconds = '-1'
time = 'unknow'
comment = 'unknow'
status = '-1'
log_v = '-1'
status_c = 'unknow'

if len(v) > 0 : 
    operator = v[0][0]
    date = v[0][1]
    last_seconds = v[0][2]
    time = v[0][3]
    comment = v[0][4]
    status = v[0][5]
    log_v = v[0][6]
    status_c = v[0][7]

'''
print operator
print date 
print last_seconds
print time
print comment
print status 
print log_v
'''
query = "select count(distinct b_id) from configure where version = %s " % (version)
b_number = get_query(query)
#print format(b_number)

query = "select count(*) from step_display where version = %s " % (version)
#print query
#print get_query(query)
total_steps = int(get_query(query))/2
#total_steps;
#date,domain,last_seconds,operator,status,status_c,time,comment,log_v,version
s = "{\"page\":1,\"total\":1,\"records\":1,\"rows\":[{\"id\":1,\"cell\":[%d,\"%s\",%s,%s,\"%s\",%s,\"%s\",\"%s\",\"%s\",%s,%s]}]}" % (total_steps,date,b_number,last_seconds,operator,status,status_c,time,comment,log_v,version)
'''
s = "{\"total\":1,\"page\":1,\"records\":6,\"rows\":[{\"id\":1,\"cell\":[{\"Tabelle\",\"1a2\",0,\"null\",\"false\",\"false\"}]},{\"id\":2,\"cell\":[\"Gestione Strutture\",\"2a2\",1,1,\"true\",\"false\"]}]}"
'''
print s
#\"<input id = '1' type = 'checkbox' value = 'yes' checked>yes</input>\"]},{\"id\":2,\"cell\":[100,200]}]}"
'''

mysql> select operator , date , last_seconds, time, comment, version, status ,log_v from ipd_conf_log where version = 2358;
+----------+------------+--------------+---------------------+-------------+---------+--------+-------+
| operator | date       | last_seconds | time                | comment     | version | status | log_v |
+----------+------------+--------------+---------------------+-------------+---------+--------+-------+
| happyhan | 07/09/2012 |        86400 | 2012-07-30 15:45:45 | jghjhghjghj |    2358 |      1 |    25 | 
+----------+------------+--------------+---------------------+-------------+---------+--------+-------+
'''

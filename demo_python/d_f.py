#!/usr/local/bin/python
import os
import cgitb
import cgi
import json
import _mysql
#import datetime

def get_user(ticket):
    f = open('ticket','r+')
    f.write(ticket)
    os.system("./ipd_get_username < ticket > ipd_get_username.out")
    f = open('ipd_get_username.out','r')
    user = f.readlines()[0]
    print 'hei' + user
    return user

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

def exe_query(query):
    con = None

    try : 
        con = _mysql.connect('localhost','root','','ip_distribution');
        con.query(query);

    except _mysql.Error, e :
        print "Error %d: %s" % (e.args[0] , e.args[1])
        sys.exit(1)

    finally:
        if con:
            con.close()

query = " select max(log_v) from ipd_conf_log";
ans = get_query(query)
if ans == None:
    ans = 0
print ans
ticket = "035002D70791EDD433B16E411BD75936F38DEFED2B7AA8D3D183127AC37735A6C29077470E6AE84B380B4205BF96870C5C44994B8ABE186FCB8D016BD10CB36CFCBFF1019FB6762C811FA6C3BD3A464FDC04E4FBBBA0DDDDFEE260B776523A447ED20E1B525AC3E4D64D168DC0FF55BEDFF45BC364520D60B1E6545A47FC797710D9836384AF5799E7AECF90B4FDB21829F42609A41CC74F75570109D8F16D98F441252575AC982963372A8623F3BA901DF39584ABD98D9647F3E7C9EBCA6FBD6D072B08A83791C7E67C3C3B14C91232"
user = get_user(ticket)
date = "2012-07-27"
last_seconds = 86400
comment = "good"
log_v = int(ans) +1
version = 2329
status = 1
status_c = "failed"
query = "insert into ipd_conf_log values('%s','%s',%d,NULL,'%s',%d,%d,%d,'%s')" % (user,date,last_seconds,comment,version,log_v,status,status_c)
print query
exe_query(query)

'''
mysql> desc ipd_conf_log;
+--------------+--------------+------+-----+-------------------+-------+
| Field        | Type         | Null | Key | Default           | Extra |
+--------------+--------------+------+-----+-------------------+-------+
| operator     | char(50)     | YES  |     | NULL              |       | 
| date         | char(20)     | YES  |     | NULL              |       | 
| last_seconds | int(11)      | YES  |     | NULL              |       | 
| time         | timestamp    | NO   |     | CURRENT_TIMESTAMP |       | 
| comment      | varchar(200) | YES  |     | NULL              |       | 
| version      | int(11)      | YES  |     | NULL              |       | 
| log_v        | int(11)      | YES  |     | NULL              |       | 
| status       | int(11)      | YES  |     | NULL              |       | 
| status_c     | varchar(200) | YES  |     | NULL              |       | 
+--------------+--------------+------+-----+-------------------+-------+
'''

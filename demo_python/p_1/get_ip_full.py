#!/usr/local/bin/python
import os
import cgitb
import cgi
import json
import _mysql
#import datetime

print "Content-type:text/html;charset=gb2312;\r\n\r\n"

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

def avl_ip(ip):
    if len(ip) < 2:
        return 0
    part = ip.split('.')
    if len(part) != 4 :
        return 0
    for single in part:
        #print single
        if int(single) < 0 or int(single) > 255 :
            return 0
    return 1

class IpInfo:
    pass
    '''
    ip_cur
    oc_id_cur
    oc_cur
    '''
form = cgi.FieldStorage()
'''
print form
value = form.getlist('ip_list')
print value
for a in value :
    print a
    '''
list_s = ''
if "ip_list" in form:
    list_s = form['ip_list'].value
#list_s = '119.84.72.51;\n3.4.6.7'
list = list_s.split('\n')
ans = []
s = '['
flag = 0
for single in list:
    #print single + 'by \\n'
    ip = single.split(';')
    for sip in ip:
        if avl_ip(sip):
            #print sip
            query = "select oc_id , oc_name from ip_oc_info where server_ip = '%s' " % (sip)
            r = get_query_r(query)
            oc_id = -1
            oc_name = 'unknown'
            if len(r) > 0:
                oc_id = r[0][0]
                oc_name = r[0][1]
            if flag > 0:
                s += ','
            s += '{"ip_cur":"'
            s += sip
            s += '"'
            s += ',\"oc_id_cur\":';
            s += format(oc_id)
            s += ','
            s += '\"oc_cur\":\"'
            s += oc_name
            s += '\"'
            s += '}'
            flag += 1
            '''
            obj = IpInfo()
            obj['ip_cur'] = sip
            obj['oc_id_cur'] = oc_id
            obj['oc_cur'] = oc_name
            ans.append(obj)
s = json.dumps(ans)
print s
'''
s += ']'
print s
#v = get_query_r(query)
#start with 0 in each row and 0 in each column
'''
operator = v[0][0]
date = v[0][1]
last_seconds = v[0][2]
time = v[0][3]
comment = v[0][4]
status = v[0][5]
log_v = v[0][6]
tatus_c = v[0][7]
'''

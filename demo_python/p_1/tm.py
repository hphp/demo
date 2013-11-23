#!/usr/local/bin/python
import os
import time
import _mysql

def hp_query(query):
    con = None

    version = -1
    try : 
        con = _mysql.connect('localhost','root','','ip_distribution')
        con.query(query)
        result = con.use_result()
        v = []
        while True:
            rows = result.fetch_row()
            if not rows : 
                break
            v.append(rows[0])

        for i in enumerate(v):
            version  = i[1][0]
            print version


    except _mysql.Error, e :
        print "Error %d: %s" % (e.args[0] , e.args[1])
        sys.exit(1)

    finally:
        if con:
            con.close()

    return version

while True :

    version = -1

    version  = hp_query("select max(version) from configure where state = 1 ")
    print 'hi' + format(version)

    if version < 0 : 
        time.sleep(6)
        print "no state = 1 -- pause"
        continue
    
    '''
    query = "select count(*) from step_display where version = %d and if_stored = 0 " % (version)
    cnt = hp_query(query)
    if(cnt > 0)
    '''


    file = time.gmtime()
    file_name = format(file.tm_year) + format(file.tm_mon) + format(file.tm_mday) + format(file.tm_hour) + format(file.tm_min) + format(file.tm_sec)
    print file_name 
    out_file = "/root/happyhan/ip_distribution/tm.out" + file_name
    print out_file
    f_tm_in = open("/root/happyhan/ip_distribution/tm.in","r+")
    content = format(version) + "\n100 100 0.85\n4\n1000\n0\n1\n1\n"
    f_tm_in.write(content)
    f_tm_in = open("/root/happyhan/ip_distribution/tm.in","r")
    print f_tm_in.readlines()
    cmd_2 = "/root/happyhan/ip_distribution/tm > " + out_file + " < /root/happyhan/ip_distribution/tm.in"
    print cmd_2
    os.system(cmd_2)
    time.sleep(6)

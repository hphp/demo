#!/usr/local/bin/python
import os
import time
import _mysql

while True :

    version = -1
    con = None

    try : 
        con = _mysql.connect('localhost','root','','ip_distribution');
        con.query("select max(version) from configure where state = 0");
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

    file = time.gmtime()
    file_name = format(file.tm_year) + format(file.tm_mon) + format(file.tm_mday) + format(file.tm_hour) + format(file.tm_min) + format(file.tm_sec)
    file_name += format(version)
    print file_name 
    cmd = "/root/happyhan/ip_distribution/utility_sh/full.sh > " + file_name
    print cmd
    os.system(cmd)
    time.sleep(6)

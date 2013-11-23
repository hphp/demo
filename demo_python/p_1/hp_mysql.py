#!/usr/local/bin/python

import _mysql
mysql_localhost='localhost'
mysql_user='root'
mysql_psw=''
mysql_database='ip_distribution'

def hp_query(query):
    con = None

    version = -1
    try : 
        con = _mysql.connect(mysql_localhost,mysql_user,mysql_psw,mysql_database)
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
            #print version


    except _mysql.Error, e :
        print "Error %d: %s" % (e.args[0] , e.args[1])
        sys.exit(1)

    finally:
        if con:
            con.close()

    return version

def get_query_r(query):

    con = None

    try : 
        con = _mysql.connect(mysql_localhost,mysql_user,mysql_psw,mysql_database)
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

def test_hp_query(query):
    if query == "" :
        query = "select count(*) from configure"
    v=hp_query(query)
    print v
def test_get_query_r(query):
    if query == "" :
        version = '2329'
        query = "select operator , date from ipd_conf_log where version = %s " % (version)
    v = get_query_r(query)
    for i in v:
        for j in i:
            print j
    #print len(v) 
    operator = 'unkown'
    date = 'unknow'

    if len(v) > 0 : 
        operator = v[0][0]
        date = v[0][1]
    print operator
    print date 

#test_hp_query("")
#test_get_query_r("")


#!/usr/local/bin/python
import os
import cgitb
import cgi
import json
import _mysql
import string
import random
#import datetime

def get_version(file):
    f = open(file,'r')
    list = f.readlines()
    version = None
    for i in list:
        version = i
    print format(version)
    return int(version)

def get_ticket():
    #query_str = "69CC232B0C36BD9229848ED633211D5212C98582C67F072EF358292BFA8B2D7BAEAD4C03963AFECDC0277F6456A0286AB35FAF8C622B6343D644818704D1CB3B1FA5ACD303267B5E81F83D37510672D7222E1D472CF551902E87D2D936E65EB1E36D23A88BD29E2893201EC488E5BC4B0B140D9D70A096EFDDD70EB6051DFD0B68D84C8B8A311F536B815E13AF40DC75C593CB3DA82520720DF5765631CE23C62B91665C8B1D467E666E9F25A41D9C4D81D78276E2A30A1D8BA2268E6A99C01D244CAFDCF73E8B3FB11E8D83D291701239266BA19A65B360"
    query_str = "nonenonenone"
    if "QUERY_STRING" in os.environ : 
        query_str = os.environ["QUERY_STRING"]
        print query_str + 'nice'
        return query_str[7:len(query_str)]
    return query_str 

def get_random_str(len):
    ans = ''
    for i in range(0,len):
        ans += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')
    return ans

def get_user(ticket):
    #print format(ticket) + 'heii' + format(len(format(ticket)))
    if len(format(ticket)) < 5 : 
        return 'none'
    random_str = get_random_str(10)
    print random_str
    file = 'ticket' + random_str
    print file
    f = open(file,'w+')
    if f.write(ticket) == None:
        f.close()

        file_out = "ipd_get_username.out" + random_str

        if os.system("./ipd_get_username < " + file + " > " + file_out) == 0 : 
            '''
            ATTENTION!!!!
            there is a problem, or bug here , if many people user this cgi and output to the same file , then maybe the system will get broken , or at least chaos.
            '''
            f = open(file_out,'r')
            lines = f.readlines()
            user = 'not_tencent_worker'
            if len(lines) > 0:
                user = lines[0]
                print 'hei' + user
            return user
        else :
            return " sorry unknown"
    else :
        return " sorry unknown"

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

def delete_n_in_comment(comment):
    string.replace(comment,'\n',';')
    return comment

def check_user_validity(user):
    avl_user_list = [
           'happyhan',
           'sidneyyu',
           'kunsonshen',
           'fredzeng',
           'cenzhao'
            ]
    for avl_u in avl_user_list:
        if user == avl_u :
            return 1
    return 0


print "Content-type:text/html\r\n\r\n"
#cgitb.enable()
form = cgi.FieldStorage()
#os.system("echo 'hi' > iii")

#dp_f = datetime.date.todkay()
#dp_t = datetime.date.today()
dp_f = "07/18/2012"
dp_t = "07/18/2012"
ticket = "nonenonenonenone"
data_range = 1800
comment = "none"
sblist_content = "[{\"b_id\":6}]"
if "dp_f" not in form : 
    #print "dp_f"
    print ""
else : 
    #print form["dp_f"].value
    dp_f = form["dp_f"].value
if "dp_t" not in form : 
    #print "dp_t"
    print ""
else : 
    #print form["dp_t"].value
    dp_t = form["dp_t"].value
if "data_range" not in form : 
    #print "data_range"
    print ""
else : 
    #print form["data_range"].value
    data_range = form["data_range"].value
if "sblist_content" not in form : 
    #print "sblist_content"
    print ""
else : 
    #print form["sblist_content"].value
    sblist_content = form["sblist_content"].value
if "comment" in form:
    comment = form["comment"].value
comment = delete_n_in_comment(comment)
#print dp_f
#print dp_t
#print data_range
#print sblist_content
#conf_file = "/usr/local/apache2/conf/ip_distribution/configure2"
conf_file = "ipd_conf"

mon = dp_t[0:2]
day = dp_t[3:5]
year = dp_t[6:10]
date = year + '-' + mon + '-' + day
content = date + ' ' + format(data_range)
#print content
f = open(conf_file,'r+')
f.write(content)

b_list = json.loads(sblist_content)
#print b_list
#print len(b_list)

for a in b_list:
    #print a["b_id"]
    print ""

iic_in = "iic.in"
f = open(iic_in,'w')
null = ""
f.write(null)
f = open(iic_in,'a')
f.write(format(len(b_list)))
f.write("\n")
for a in b_list:
    f.write(format(a["b_id"]))
    f.write("\n")

print f
f = open(iic_in,'r')
print f.readlines()
#os.system("echo 'hi'");
'''
ATTENTION : there is a bug here , too , it is similar with bug above , because it 
'''
os.system("./iic_v_b < iic.in > iic.out")
version = get_version("iic.out")

query = " select max(log_v) from ipd_conf_log"
ans = get_query(query)
print ans
if ans == None:
    ans = 0
print ans
ticket = get_ticket()
print ticket
#"035002D70791EDD433B16E411BD75936F38DEFED2B7AA8D3D183127AC37735A6C29077470E6AE84B380B4205BF96870C5C44994B8ABE186FCB8D016BD10CB36CFCBFF1019FB6762C811FA6C3BD3A464FDC04E4FBBBA0DDDDFEE260B776523A447ED20E1B525AC3E4D64D168DC0FF55BEDFF45BC364520D60B1E6545A47FC797710D9836384AF5799E7AECF90B4FDB21829F42609A41CC74F75570109D8F16D98F441252575AC982963372A8623F3BA901DF39584ABD98D9647F3E7C9EBCA6FBD6D072B08A83791C7E67C3C3B14C91232"
user = get_user(ticket)
validity = check_user_validity(user)
print validity
if validity == 0 :
    print '<script type = "text/javascript">alert("invalid user , please contact happyhan for rights")</script>'
    print "<meta http-equiv=\"refresh\" content=\"3; url=http://passport.oa.com/modules/passport/signin.ashx?url=http://172.27.200.198/ip_distribution/ipd_config.html\" />"
else : 
    date = dp_t
    last_seconds = int(data_range)
    log_v = int(ans) +1
    status = 1
    status_c = "success"
    query = "insert into ipd_conf_log values('%s','%s',%d,NULL,'%s',%d,%d,%d,'%s')" % (user,date,last_seconds,comment,version,log_v,status,status_c)
    print query
    exe_query(query)

    for a in b_list:
        b_id = a["b_id"]
        query = "insert into ipd_conf_log_b values(%d,%d)" % (log_v,b_id)
        print query
        exe_query(query)

    query = "insert into version_info values(%d,0)" % (version)
    exe_query(query)

    print "success"
    '''
    src = "<iframe id = 'wc' src = '../../htdocs/ip_distribution/ipd_stratergy.html?ticket=";
    src += ticket;
    src += "'></iframe>";
    print src
    '''
    print "<meta http-equiv=\"refresh\" content=\"3; url=http://passport.oa.com/modules/passport/signin.ashx?url=http://172.27.200.198/ip_distribution/ipd_stratergy.html?ipd_strtg_type=effective\" />"

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

    mysql> desc ipd_conf_log_b;
    +-------+---------+------+-----+---------+-------+
    | Field | Type    | Null | Key | Default | Extra |
    +-------+---------+------+-----+---------+-------+
    | log_v | int(11) | YES  |     | NULL    |       | 
    | b_id  | int(11) | YES  |     | NULL    |       | 
    +-------+---------+------+-----+---------+-------+
    '''

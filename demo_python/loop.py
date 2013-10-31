#!/usr/local/bin/python

class File:
    dis_time=0
    url=""
    filename=""
def get_list():
    list=[]
    for i in range(5):
        v=File()
        v.dis_time=i*100
        if i < 2 :
            v.url = "http://172.27.208.76/ip_distribution/ipd_v0.2.tar"
        else :
            v.url = "http://172.27.208.76/ip_distribution/help/ipd_0_1.sql"
        v.filename = "file" + str(i)
        list.append(v)
    return list

def test_get_list():
    v_list=get_list()
    for i in range(len(v_list)):
        print v_list[i].dis_time
        print v_list[i].url
        print v_list[i].filename
        print "good"
test_get_list()

#!/bin/sh

test_send_header(){
    #curl -I 172.27.208.76/ip_distribution/home.html
    #below url could get 304 , if last_modified =Tue, 21 Aug 2012 11:14:15 GM
    #test for diff time of diff day in the same month , get 304 , but when month have been changed , 200 ,supposed to be the server error.
    #curl --header "If-Modified-Since: Sat, 21 Jul 2012 22:14:15 GMT" 172.27.208.76/ip_distribution/home.html -I
    #below url could get 304 , if last_modified =Tue, 21 Aug 2012 11:14:15 GM
    #curl --header "If-Modified-Since: Tue, 21 Aug 2012 22:14:15 GMT" 172.27.208.76/ip_distribution/home.html -I
    #below url could get 304 , if last_modified =Tue, 21 Aug 2012 11:14:15 GM
    #curl --header "If-Modified-Since: Tue, 21 Aug 2012 12:14:15 GMT" 172.27.208.76/ip_distribution/home.html -I
    #below url get 200 , if last_modified =Tue, 21 Aug 2012 11:14:15 GM , even if the date change to from 2 to 02 , nothing chagnes.
    #curl --header "If-Modified-Since: Sun, 02 Sep 2012 12:14:15 GMT" 172.27.208.76/ip_distribution/home.html -I
    #curl --header "If-Modified-Since: Tue, 21 Aug 2012 11:14:15 GMT" 172.27.208.76/ip_distribution/home.html -I
    curl --header "If-Modified-Since: 2012-08-21 11:14:15 UTC" 172.27.208.76/ip_distribution/home.html -I
}
#test_send_header

test_curl_basic(){
# this curl runs linearly
# adding -C - both , and both download things conintuely
# add one -C - , both download continously
# delete all -C - , re download.
curl --limit-rate 2K 172.27.208.76/ip_distribution/home.html -C - -o home.html 172.27.208.76/ip_distribution/ipd_config.html -C - -o config.html
}
#test_curl_basic

test_get_curl_header(){
    # -I means that get headers only
    # -s means that did not output the transforming info
    s=$(curl 172.27.208.76/ip_distribution/home.html -s -I | grep "Server" | awk '{print $2}')
    echo $s
}
#test_get_curl_header

test_get_curl_header_spc(){
    param=$1
    s=$(curl 172.27.208.76/ip_distribution/home.html -s -I | grep "$param" | awk '{print $2}')
    echo $s
}
#test_get_curl_header_spc "Server"
#s=$(test_get_curl_header_spc "Content-Length" | grep  -Eo "[0-9]+")
#echo $s

test_get_status_code(){
    url=$1
    s=$(curl -s -I "$1" | awk 'NR>1{exit};{print $2}')
    echo $s
}
#test_get_status_code 172.27.208.76/ip_distribution/home.html

test_curl_error(){
    #curl -I dlql.qq.com/dl_dir3.qq.com/minigamefile/zhaocha/smallpic/pic297_5.pkg 2>x
    curl -I 172.27.208.76/ip_distribution/home.html 2>x
    read line < "x"
    echo $line
    if [ "$line" == "HTTP/1.1*" ]; then
    #if [ "$line" == "curl: (7) couldn't connect to host" ]; then
        echo everythings fine
    else
        echo error:$line
    fi
#echo $s
}
#test_curl_error


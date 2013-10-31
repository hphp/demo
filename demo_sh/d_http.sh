#!/bin/sh

<<COMMENT
check if modify :
check the mtime 
request url if-modified-since:mtime
    if stat-code == 304
        not modify
    else
        modified
    fi
request url:NEED
1.how to construct header using curl - done - curl --header "$header"
2.how to change mtime to GMT format - done - date --date="anyformat" +[format]
3.test if return code 304
COMMENT

get_time(){
    url=$1
    param=$2
    curl -s -I $url | grep $param | awk -F ':' '{print $2":"$3":"$4}'
}

check_if_modify(){
    url=$1
    local_file=$2
    mtime=$(stat -c %y "$local_file")
    echo mtime:$mtime

    Last_Modified=$(curl -s -I $url | grep "Last-Modified:" | awk -F ':' '{print $2":"$3":"$4}')
    echo last_modify:$Last_Modified
    d_last_modifed=$(date --date="$Last_Modified" -u +"%Y-%m-%d %H:%M:%S %Z")
    echo d_last_mdify:$d_last_modifed
    d_mtime=$(date --date="$mtime" -u +"%Y-%m-%d %H:%M:%S %Z")
    echo d_mtim:$d_mtime

    if [ "$d_mtime" == "$d_last_modifed" ]; then
        echo good equal
    else
        echo not equal
    fi
}

time_diff(){
    time1=$1
    time2=$2
    expr $(date --date="$time1" +"%s") - $(date --date="$time2" +"%s")
}

weekdays=(0 "Mon" "Tue" "Wed" "Thu" "Fri" "Sat" "Sun")
months=(null "Jan" "Feb" "Mar" "Apr" "May" "Jun" "Jul" "Aug" "Sep" "Oct" "Nov" "Dec")
#echo ${months[01]}
check_if_modify_2(){
<<COMMENT
0.check if this server have a same time with the url server , using http header.
1.get mtime of localfile ,
2. send if_modified_since mtime to get header using curl
3. check response status code , if 304 , not modified.

NEED:
1.date -u localdate , and print chinese sometimes. - done , we use number to get english format
COMMENT
    url=$1
    local_file=$2

    #check if client time be around server time
    time1=$(date)
    time2=$(get_time $url "Date")
    diff=$(time_diff "$time1" "$time2")
    echo $diff

    if_ex=$(echo god | awk -v v=$diff '{if($v > 10000){print "1"}else{print "0"}}')
    echo $if_ex
    if [  $if_ex == "1" ]; then
        echo not gooddddddddddddd
        return 1
    fi


    mtime=$(stat -c %y "$local_file")
    echo mtime:$mtime

    weekday=$(date --date="$mtime" +"%u")
    mon=$(date --date="$mtime" +"%m")
    date=$(date --date="$mtime" +"%e")
    year=$(date --date="$mtime" +"%Y")
    time=$(date --date="$mtime" +"%H":"%M":"%S")
    echo $weekday > ttt
    weekday=$(sed "s/^[0]*//g" ttt)
    echo $mon > ttt
    mon=$(sed "s/^[0]*//g" ttt)
    echo ${weekdays[$weekday]}
    echo ${months[$mon]}
    gmt_mtime=${weekdays[$weekday]}", "$date" "${months[$mon]}" "$year" "$time" GMT"
    echo $gmt_mtime
    request_header="If-Modified-Since: "$gmt_mtime
    curl --header $request_header -s -I $url
    return_code=$(curl --header $request_header -s -I $url | awk 'NR > 1{exit 1}{print $2}')
    echo $return_code
<<COMMENT
    Last_Modified=$(curl -s -I $url | grep "Last-Modified:" | awk -F ':' '{print $2":"$3":"$4}')
    echo last_modify:$Last_Modified
    d_last_modifed=$(date --date="$Last_Modified" -u +"%Y-%m-%d %H:%M:%S %Z")
    echo d_last_mdify:$d_last_modifed
    d_mtime=$(date --date="$mtime" -u +"%Y-%m-%d %H:%M:%S %Z")
    echo d_mtim:$d_mtime

    if [ "$d_mtime" == "$d_last_modifed" ]; then
        echo good equal
    else
        echo not equal
    fi
COMMENT
}
check_if_modify_2 "172.27.208.76/ip_distribution/home.html" "/root/happyhan/dl_support/ds_script/data/home.html"

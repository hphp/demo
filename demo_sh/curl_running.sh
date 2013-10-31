#!/bin/sh

curl_p_whole="bash"


get_length(){
    #same reason - quotes
    return $(expr length "$1")
}
get_total_length(){
    return ${#1}
}
get_suffix(){

    line=$1
    sub=$2
    get_length "$line"
    len=$?
    get_length "$sub"
    sublen=$?
    s=$(expr $len - $sublen)
    e=$len

    echo ${line:$s:$e}
}

cmp_str(){
    if_e=$(expr "$1" == "$2")
    return $if_e
}

is_suffix(){

    ori_sub="$2"
    sub=$(get_suffix "$1" "$2")
    cmp_str "$ori_sub" "$sub"
    w_e=$?
    return $w_e
}

is_curl_running=1
curl_running(){

    flag=0
    ps a | while read line
    do  
        echo isr$is_curl_running
        #echo psline:$line
        #echo curl_p_whole:$curl_p_whole
        is_suffix "$line" "$curl_p_whole"
        ans=$?
        echo is_suffixxx:$ans
        if [ $ans == 1 ];then
            echo curl_running-find it!!!!
            is_curl_running=1
            echo in_is_r$is_curl_running
        fi  
    done
    echo last_is_r$is_curl_running
}
test_curl_running(){
    curl_running
    sleep 3
    echo ee$is_curl_running
}

curl_pid=8144
curl_p_whole="curl -C - -o cur_8 --limit-rate 10K -m 600 http://172.27.208.76/ip_distribution/help/ipd_0_1.sql"

curl_running_2(){
    results=$(ps $curl_pid)
    echo $results
    is_suffix "$results" "$curl_p_whole"
    ans=$?
    echo $ans
}
curl_running_2

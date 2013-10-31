#!/bin/sh

get(){
    #return 10000 =-- the result is 16.amzing.
    return 256 
}

basic_test(){
get
s=$?
echo s:$s
}

get_length(){
    #same reason - quotes
    #echo length:$1
    #       expr length "$1"
    sss=$1
    #echo sss:$sss
    echo ${#sss}
}

test_function_in_function(){
ss="$1"
s=`get_length "$ss"`
echo s:$s
}

fff(){
test_function_in_function "$1"
}

ffff(){
fff "$1"
}
ffff "curl -C - -o /data/dlcenterfile/dlied1.qq.com/qqkart/full/QQSpeed1.00_Beta40_Build005_20120816.exe_happy --limit-rate 2G -m 600 dlql.qq.com/dlied1.qq.com/qqkart/full/QQSpeed1.00_Beta40_Build005_20120816.exe"




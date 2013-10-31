#!/bin/sh

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
test_is_suffix(){
    read line1
    read line2
    echo $line1
    echo $line2
    is_suffix "$line1" "$line2"
    ans=$?
    echo $ans
}
test_get_length(){
    read line
    echo $line
    #it is very important to contain the quotes below, because when line have space , it will be treated as several arguments that should pass through to the function get_length or get_total_length
    get_length "$line"
    len=$?
    echo $len
}
test_total_length(){
    read line
    echo $line
    get_total_length "$line"
    len=$?
    echo $len
}
test_get_suffix(){
    read l1
    read l2
    suffix=$(get_suffix "$l1" "$l2")
    echo $suffix
}
#test_get_length
test_is_suffix
#test_total_length
#test_get_suffix

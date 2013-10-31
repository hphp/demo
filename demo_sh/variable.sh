#!/bin/sh

curl_p_whole="bash"

cmp_str(){
    if_e=$(expr "$1" == "$2")
    return $if_e
}

test_change_global_variable(){
    ps a | while read line
    do
        echo $line
        cmp_str "$line" "good"
        ans=$?
        echo $ans
        if [ $ans == 0 ] ; then
            curl_p_whole="xx"
        else
            echo no
        fi
    done
}
#read line
test_change_global_variable $line
echo $curl_p_whole

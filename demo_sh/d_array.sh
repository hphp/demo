#!/bin/sh


test_start_from(){
    a=[]
    echo ${#a}
    echo ${a[0]}","${a[1]}","${a[2]}
    a
    echo ${#a}
    echo ${a[0]}","${a[1]}","${a[2]}
    a=()
    echo ${#a}
    echo ${a[0]}","${a[1]}","${a[2]}
}
test_start_from


basic_test(){
    a=[]
    a[0]=1
    a[1]=2
    echo ${#a[@]}

    for (( i = 0 ; i < ${#a[@]} ; i ++))
    do
        a[$i]=3
        echo ${a[$i]}
    done
    echo start
    for ((i = 0 ; i < ${#a[@]} ; i ++))
    do
        echo ${a[$i]}
    done
}

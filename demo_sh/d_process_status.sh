#!/bin/sh

assist(){
    while true
    do
        echo "yes,i'm running"
        sleep 2
    done
}

assist &
son_pid=$!
echo $son_pid 

while true
do
    read line
    if [ $line -eq 1 ];then
        #if [ ]
        kill -STOP $son_pid
    elif [ $line -eq 2 ];then
        kill -CONT $son_pid
    elif [ $line -eq 3 ];then
        kill $son_pid
    fi
done


#!/bin/sh

#set -x

#check for the disk usage , if usage > 60% , echo 1 
checkLog=logs/disk_log
fullFlag=0
iostat -d -x >> $checkLog
percent_list=$(cat $checkLog | awk '{print $14}' | grep -Eo "[0-9]+")
#echo $percent_list
for num in $percent_list
do
    if [ $num -ge 50 ]; then
        fullFlag=1
    fi
    break
done

#chek for the disk 

if [ $fullFlag -eq 1 ]; then
    echo 1
fi


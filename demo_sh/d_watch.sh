#!/bin/sh

while true
do
    re=`ps -ef | grep "dl_get_file_happy_sim.sh" | grep "/bin/sh"`
    if [ "$re" == "" ];then
        date=`date +%s`
        echo "["$date"]" "["not working , nohup now"]" >> watch_log
        nohup ./dl_get_file_happy_sim.sh &
    else
        date=`date +%s`
        echo "["$date"]" "["working fine"]" >> watch_log
    fi
    sleep 1
done

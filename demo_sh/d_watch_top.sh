#!/bin/sh

<<COMMENT
  PID USER      PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+  COMMAND                                                                
  17970 root      16   0  661m 553m 1264 S    3  6.9  44:21.88 nws                                                                    
  14774 root      16   0  151m  72m  31m S    1  0.9  66:46.48 qnf                                                                    
  18894 root      15   0  9504 3332  996 S    1  0.0   8:27.36 data_pipe 
COMMENT

while true
do
    re=`top -n 1 b | awk '{if($9 > 40)print $0}' | grep "dl_get_file_ha"`
    if [ "$re" == "" ];then
        date=`date +%s`
        echo $date"|occupy not more than limit" >> watch_log
    else
        date=`date +%s`
        echo $date"|kill" >> watch_log
        pkill -9 -f dl_get_file_happy_sim.sh
    fi
done


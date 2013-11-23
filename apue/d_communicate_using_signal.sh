#!/bin/sh

(./d_communicate_using_signal & echo $! >pid) | while read line line2
do
	echo "we've read "$line
	echo "hei"$line2
	pid=$(<pid)
	echo $pid
	cnt=0
	while true
	do
		./send_signal.sh $pid 10
		returnc=$?
		echo $returnc
		if [ $returnc -eq 0 ] ; then
			break
		fi
		cnt=`expr $cnt + 1`
		if [ $cnt -gt 10 ];then
			cnt=0
			log_content="cant set signal SIGUSR1 to data_pipe, with returncode:"$returnc
			/usr/local/agenttools/agent/agentRepStr 200931 "$log_content"
		fi
	done
	sleep 1
done


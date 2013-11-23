#!/bin/sh

c=0
while true
do
	c=$(( $c + 1))
	if [ $c -gt 2 ];then	
		break
	fi
	echo $$
	sleep 1
done

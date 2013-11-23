#!/bin/sh

cnt=0
while true
do
	echo good
	if [ $cnt -gt 1000000 ];then
		break
	fi
	cnt=`expr $cnt + 1`
done

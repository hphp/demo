#!/bin/sh

st=1
if [ "$1" != "" ];then
	st=$1
fi

while read len
do
	echo $len 
	if [ $st -lt 2 ];then
		if [ $st -gt 0 ];then
			echo $len > output
		fi
	fi
	sleep $st 
done

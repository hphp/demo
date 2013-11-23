#!/bin/sh

total_random=`od -An -N2 -i /dev/random`
a=0
random=`od -An -N2 -i /dev/random`
while true
do
	if [ $a -gt $total_random ];then
		break
	fi
	echo $random$random 
	a=`expr $a + 1`
	am=`expr $random % $a`
	if [ $am -eq 0 ];then
		random=`od -An -N2 -i /dev/random`
	fi
	random=`expr $random - 1`
done


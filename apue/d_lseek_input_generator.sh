#!/bin/sh

a=0
s=""
while true
do
	s=""
	for(( i = 0 ;i < 10 ;i ++))
	do
		s=$s""$a
	done
	echo $s >> d_lseek.in
	a=`expr $a + 1`
	sleep 5
done

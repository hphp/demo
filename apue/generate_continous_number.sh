#!/bin/sh

a=0
while true
do
	a=`expr $a + 1`
	#echo $a
# >> d_read.in
	#echo $a >> d_read.std
	./pipe.sh $a &
done

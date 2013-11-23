#!/bin/sh

x=0
while true
do
    echo $x >> $1
    x=$(($x + 1))
    if [ $x -gt 100000000 ] ; then
        break;
    fi
done

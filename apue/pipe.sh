#!/bin/sh

rand=`expr $RANDOM % 10`
sleep $rand
echo $1

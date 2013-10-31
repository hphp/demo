#!/bin/sh

s=`ps -ef | grep "curl" | grep "x_happy"`
echo $s
if [ "$s" == "" ];then
    echo null
else
    echo good $s
fi

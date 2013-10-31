#!/bin/sh

line3=[]

cnt=0
while read line line2
do
    echo $line
    echo $line2
    line3[$cnt]=$line
    cnt=$(expr $cnt + 1)
done < temp
echo final:${#line3[@]}

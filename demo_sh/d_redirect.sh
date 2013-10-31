#!/bin/sh

md5sum a | while read line
do
    echo "hi:"$line
done
#doesnt work

#read line
#echo $line
#md5sum a | x x command not found


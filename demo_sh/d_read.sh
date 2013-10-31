#!/bin/sh

while read a b c d
do
    echo a:$a";b:"$b";c:"$c";d:"$d";"
    if [ "$d" == "" ];then
        echo null
    fi
    if [ $d == null ];then
        echo null
    fi
done

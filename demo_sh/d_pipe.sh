#!/bin/sh

./output_1.sh | ./output_2.sh | while read a
do
    echo $a
    sleep 5
done

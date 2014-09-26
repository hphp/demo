#!/bin/sh
awk '{a[$1]+=$2}END{for(ele in a)print ele,a[ele]}'

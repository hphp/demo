#!/bin/sh
awk -F ' ' '{for(i=1;i<=NF;i++)a[$i]+=1}END{for(ele in a)print ele,a[ele]}'

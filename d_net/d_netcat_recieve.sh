#!/bin/sh

netcat -l -p 1111 > 1111.out
cat 1111.out | netcat -c localhost 1122
#| netcat localhost 1111
echo $?
#cat d_netcat_send.out | netcat localhost 1111

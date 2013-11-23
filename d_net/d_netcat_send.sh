#!/bin/sh

./get_time
cat d_netcat_send.in | netcat -c localhost 1111 
netcat -l -p 1122 > 1122.out
#netcat -l -p 1111 > d_netcat_send.xx
./get_time


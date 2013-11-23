#!/bin/sh

#./d_unbuffer_read_in.sh | ./d_unbuffer_read_in.sh | ./d_unbuffer_read_in.sh 10 # this one , the output change really fast 
./d_unbuffer_read_in.sh 0 | unbuffer -p ./d_unbuffer_read_in.sh | ./d_unbuffer_read_in.sh 10 # this one , the output change as the last d_unbuffer_read_in reads. 


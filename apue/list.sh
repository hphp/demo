#!/bin/sh
echo "1.have in mind that when testing IO  , take care of the pipe buffer size"

echo "1.d_read_control_write.cpp	-->	while output always as pipe buffer size , so that as soon as the read is blocking , it wont write at all"

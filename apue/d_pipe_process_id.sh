#!/bin/sh

(../../utility/always_running.sh & echo $! >pid) | while read line
do
	echo "here,we have read"$line
	echo $(<pid)
done


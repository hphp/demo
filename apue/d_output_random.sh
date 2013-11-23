#!/bin/sh

./random_output.sh | while read file
do
	./write.sh "$file" | ./read_in.sh &	
done 

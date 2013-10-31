#!/bin/sh

read_from_process(){
    ./hello | while read lines
    do
        echo "good_"$lines
    done
}
read_from_process_with_array(){
    cnt=0
    ./hello | while read lines[$cnt]
    do
        echo "good_"${lines[$cnt]}
        cnt=$( expr $cnt + 1 )
    done
}
read_from_several_input(){
    ./watch.py | while read lines
    do
        echo $lines
        echo 'hi'
        ps a | while read line
        do
            echo 'xx'$line
        done
    done
}
read_from_several_input
#read_from_process_with_array

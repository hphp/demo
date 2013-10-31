#!/bin/sh

get_pid(){
    s=$$
    echo $s
    echo $!
}

get_ps_info(){
    ps a | grep "curl" | while read line
    do
        echo $line
    done
}

get_ps_info

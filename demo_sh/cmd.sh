#!/bin/sh

cmd_output(){
    watch=$(./watch.py)
    echo good
    echo $watch
}

cmd_output_gps(){
    returnv=$(ps a | grep "curl")
    echo $returnv
}

cmd_output_ps(){
    returnv=$(ps a | grep "curl")
    echo $returnv
}

#cmd_output
cmd_output_ps


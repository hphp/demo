#!/bin/sh

get_file_size(){
filesize=$(stat -c '%s' main.sh)
echo $filesize
}
if_file_exists(){
    file=$1
    if [ -f $file ]; then
        echo exists
    else
        echo not exists
    fi
}
#if_file_exists "/root/happyhan/.vimrc"
#if_file_exists "/root/happyhan/.imrc"
if_dir_exists(){
    dir=$1
    if [ -d $dir ]; then
        echo exists
    else
        echo not exists
    fi
}
#if_dir_exists "/root/happyhan/.vimrc"
#if_dir_exists "/root/happyhan/"
if_dir_exists "/"


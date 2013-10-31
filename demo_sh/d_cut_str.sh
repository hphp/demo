#!/bin/sh

str="bc"
path="abcdefghijk"
echo ${#str}
echo ${path:${#str}+1:${#path}}

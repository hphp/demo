#!/bin/sh
# does not work ~
declare -A animals
animals=( ["aa"]="bb" )
declare -A animals=( ["cc"]="dd" )

echo ${animals["aa"]}
for sound in ${!animals[@]} 
do
    echo $sound - ${animals[$sound]}
done

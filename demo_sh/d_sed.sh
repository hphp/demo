#!/bin/sh

#x="0033045000"
echo $x | sed "s/^[0]*/1/g"

echo abcd\" | sed "s/\"//"

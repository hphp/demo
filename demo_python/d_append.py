#!/usr/bin/python
import json

b_list = ["a","b"]
iic_in = "iic.in"
f = open(iic_in,'w')
null = ""
f.write(null)
f = open(iic_in,'a')
f.write(format(len(b_list)))
f.write("\n")
for a in b_list:
    f.write(a)
    f.write("\n")

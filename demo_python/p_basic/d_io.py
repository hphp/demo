#!/usr/bin/python
import sys

f = sys.stdin
line = f.readline()
while line:
	print line # line with /n
	print line.rstrip()
	line = f.readline()

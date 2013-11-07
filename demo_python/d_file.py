#!/usr/bin/python
import os
f = open('test','w')
f.write('xx')
f.write('yy')
f.writelines('xm')
# above is append
f.writelines('nnn' + os.linesep)
# append and set tail to a new line.
f.close()

#!/usr/bin/python
import Image

im = Image.new("RGB", (124, 124), "white")
cpjpg = Image.open("cp.jpg")
#x.show()

#x = Image.new("RGB", (157,80))
x = cpjpg.copy()
x.paste(cpjpg,(0,0))
##the cpjpg is pasted to x . and box ( a , b ) means that paste to x start from .(a,b) source from cpjpg.(0,0) .
x.paste(cpjpg,(0,0,311,162))
# when it is a 4-tuple l,u,r,lower , the size of the pasted image should equal to the region.....
#x.paste(cpjpg,(0,0,311,162))

x.show()
cpjpg.show()

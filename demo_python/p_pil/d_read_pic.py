#!/usr/bin/python
import os,sys
import Image


# rawfile = open("cp.jpg")
# hex_data = rawfile.read() # it is a bunch of meaningless chars..
# print hex_data

jpgfile = Image.open("cp.jpg")
pix_list = list(jpgfile.getdata()) # shows a list of pixel data from this picture.
# print pix_list
for ele in pix_list:
	break
	# print ele # this ele is a 3-ele-list
	for e in ele:
		print e
#print len(pix_list) # total 2D grids number
#print pix_list[a*width + b] # the corresponding pixels
width,height = jpgfile.size
print height
print width
# print pix_list[ y * width + x ]

# jpgfile.show() # show it in preview-mac ;
#print jpgfile.bits, jpgfile.size, jpgfile.format

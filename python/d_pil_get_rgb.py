#!/usr/bin/python

from PIL import Image
img = Image.open("cat.5123.jpg")
rgbimg = img.convert('RGB')
for i in range(5):
    print rgbimg.getpixel((i, 0))
    print type(rgbimg.getpixel((i,0)))

#!/usr/bin/python

from PIL import Image
import colorsys

img = Image.open("cat.5123.jpg")
#rgbimg = img.convert('RGB')
rgbimg = img
print type(rgbimg)
for i in range(140,150):
    rgb_v = rgbimg.getpixel((i, 144))
    print rgb_v,type(rgb_v)
    hsv_l = colorsys.rgb_to_hsv(rgb_v[0],rgb_v[1],rgb_v[2])
    print hsv_l , type(hsv_l)

#!/usr/bin/python

from PIL import Image,ImageEnhance,ImageFilter

image_name="cat.5123.jpg"
im = Image.open(image_name)
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
im.show()
im.save("1.jpg")

#!/usr/bin/python

from PIL import Image,ImageEnhance,ImageFilter
import numpy

def load_img_to_list():
    image_name="cat.5123.jpg"
    im = Image.open(image_name)
    print im.size
    data = im.getdata()
    print type(data),len(data) # type:ImgCore , 
    data = list(im.getdata())
    print type(data),len(data),data[0] # type:list,len:h*w,(R,G,B)

def test_hw_order():
    image_name="cat.5123.jpg"
    img = Image.open(image_name)
    print img.size
    img_numpy = numpy.asarray(img, dtype='int')
    img_list = list(img.getdata())
    img_w, img_h = img.size
    count = 0
    for h in range(img_h):
        for w in range(img_w):
            rgb_numpy = img_numpy[h][w]
            rgb_list = img_list[h*img_w + w]
            for i in range(len(rgb_list)):
                rgb_numpy_v = int(rgb_numpy[i])
                rgb_list_v = int(rgb_list[i])
                if rgb_numpy_v != rgb_list_v :
                    count += 1
    print count
#load_img_to_list()
test_hw_order()

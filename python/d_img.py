#!/usr/bin/python

from PIL import Image,ImageEnhance,ImageFilter
import numpy
import cv2
import pylab

def random_pixel_img():
    rng = numpy.random.RandomState(22222)
    rand_l = rng.uniform(0, 255, size=(50, 50))
    mode = 'RGBA'
    size = (50, 50)
    n_img = Image.frombuffer(mode, size, rand_l.tostring(), 'raw', mode, 0, 1)
    pylab.axis('off'); pylab.imshow(n_img)
    pylab.show()

def show_img():
    img = Image.open('cat.5123.jpg')
    pylab.axis('off'); pylab.imshow(img)
    pylab.show()

def PIL2array():
    img = Image.open('cat.5123.jpg')
    pylab.axis('off'); pylab.imshow(img)
    pylab.show()
    return (numpy.array(img.getdata(), numpy.uint8).reshape(img.size[1], img.size[0], 3), img.size)

def array2PIL():
    arr, size = PIL2array()
    print size
    mode = 'RGBA'
    arr = arr.reshape(arr.shape[0]*arr.shape[1], arr.shape[2])
    if len(arr[0]) == 3:
        arr = numpy.c_[arr, 255*numpy.ones((len(arr),1), numpy.uint8)]
    n_img = Image.frombuffer(mode, size, arr.tostring(), 'raw', mode, 0, 1)
    pylab.axis('off'); pylab.imshow(n_img)
    pylab.show()

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
#test_hw_order()
#array2PIL()
#show_img()
random_pixel_img()

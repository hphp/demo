#!/usr/bin/python

'''
    written by hp_carrot
    2013-11-13
    load picture and get some hsv values.
'''

import numpy
import pylab
from PIL import Image
import colorsys

img = Image.open(open("cat.5123.jpg"))
#img = img.resize((200,200),Image.ANTIALIAS)
img_w , img_h = img.size
print img.size
img = numpy.asarray(img, dtype='float32') / 256
print img[0][0]
rgb = img[0][0]
print type(rgb) , rgb.shape , rgb
hsv = colorsys.rgb_to_hsv(rgb[0],rgb[1],rgb[2])
print type(hsv),hsv
'''
print img.shape
type of img :  <type 'numpy.ndarray'> (285, 304, 3)
type of swapaxes(0,2): <type 'numpy.ndarray'> (3, 304, 285)
type of swapaxes(0,2).swapaxes(1,2): <type 'numpy.ndarray'> (3, 285, 304)
type of swapaxes(0,2).swapaxes(1,2).reshape(1,3,img_h,img_w): <type
'numpy.ndarray'> (1, 3, 285, 304)
'''

'''
# put image in 4D tensor of shape (1, 3, height, width)
img_ = img.swapaxes(0, 2).swapaxes(1, 2).reshape(1, 3, img_h, img_w)
print "type of img : ", type(img) , img.shape
print "type of swapaxes(0,2):" ,type(img.swapaxes(0,2)) ,img.swapaxes(0,2).shape
print "type of swapaxes(0,2).swapaxes(1,2):" ,type(img.swapaxes(0,2).swapaxes(1,2)) ,img.swapaxes(0,2).swapaxes(1,2).shape
print "type of swapaxes(0,2).swapaxes(1,2).reshape(1,3,img_h,img_w):" ,type(img.swapaxes(0,2).swapaxes(1,2).reshape(1,3,img_h,img_w)) ,img.swapaxes(0,2).swapaxes(1,2).reshape(1,3,img_h,img_w).shape
'''
'''
filtered_img = f(img_)

# plot original image and first and second components of output
pylab.subplot(1, 3, 1); pylab.axis('off'); pylab.imshow(img)
pylab.gray();
# recall that the convOp output (filtered image) is actually a "minibatch",
# of size 1 here, so we take index 0 in the first dimension:
pylab.subplot(1, 3, 2); pylab.axis('off'); pylab.imshow(filtered_img[0, 0, :, :])
pylab.subplot(1, 3, 3); pylab.axis('off'); pylab.imshow(filtered_img[0, 1, :, :])

# filter_img.shape = (1,2,img_h,img_w)
print type(filtered_img),filtered_img.shape
print type(filtered_img[0,0,:,:]),filtered_img[0,0,:,:].shape
#print type(img),img.shape
pylab.show()
'''

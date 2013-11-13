#!/usr/bin/python

'''
    modified by hp_carrot
    2013-11-04
    wanna see how image will be after outline-filtered.
    the results goes well.

    modified by hp_carrot
    2013-11-08
    see detail of convolution calculation
    conv2d(input,W)
    input.shape = [mini-batch size,feature maps number, img-h ,img-w]
    W.shape = [ feature maps number of m layer , fmn of m-1 layer , filter h,
    filter -w ]
'''

import numpy
import pylab
from PIL import Image
import theano
import theano.tensor as T
from theano.tensor.nnet import conv
rng = numpy.random.RandomState(23455)

# instantiate 4D tensor for input
input = T.tensor4(name='input')

# initialize shared variable for weights.
w_shp = (2, 3, 9, 9)
w_bound = numpy.sqrt(3 * 9 * 9)
W = theano.shared( numpy.asarray(rng.uniform( \
                    low=-1.0 / w_bound, \
                    high=1.0 / w_bound, \
                    size=w_shp), \
                dtype=input.dtype), \
            name \
            ='W')

# initialize shared variable for bias (1D tensor) with random values
# IMPORTANT: biases are usually initialized to zero. However in this
# particular application, we simply apply the convolutional layer to
# an image without learning the parameters. We therefore initialize
# them to random values to "simulate" learning.
b_shp = (2,)
b = theano.shared(numpy.asarray(rng.uniform(low=-.5, high=.5, size=b_shp),dtype=input.dtype), name ='b')

# build symbolic expression that computes the convolution of input with filters
# in w
conv_out = conv.conv2d(input, W)

# build symbolic expression to add bias and apply activation function, i.e.
# produce neural net layer output
# A few words on ``dimshuffle`` :
#   ``dimshuffle`` is a powerful tool in reshaping a tensor;
#   what it allows you to do is to shuffle dimension around
#   but also to insert new ones along which the tensor will be
#   broadcastable;
#   dimshuffle('x', 2, 'x', 0, 1)
#   This will work on 3d tensors with no broadcastable
#   dimensions. The first dimension will be broadcastable,
#   then we will have the third dimension of the input tensor as
#   the second of the resulting tensor, etc. If the tensor has
#   shape (20, 30, 40), the resulting tensor will have dimensions
#   (1, 40, 1, 20, 30). (AxBxC tensor is mapped to 1xCx1xAxB tensor)
#   More examples:
#    dimshuffle('x') -> make a 0d (scalar) into a 1d vector
#    dimshuffle(0, 1) -> identity
#    dimshuffle(1, 0) -> inverts the first and second dimensions
#    dimshuffle('x', 0) -> make a row out of a 1d vector (N to 1xN)
#    dimshuffle(0, 'x') -> make a column out of a 1d vector (N to Nx1)
#    dimshuffle(2, 0, 1) -> AxBxC to CxAxB
#    dimshuffle(0, 'x', 1) -> AxB to Ax1xB
#    dimshuffle(1, 'x', 0) -> AxB to Bx1xA
output = T.nnet.sigmoid(conv_out + b.dimshuffle('x', 0, 'x', 'x'))

# create theano function to compute filtered images
f = theano.function([input], output)

# open random image of dimensions 639x516
img = Image.open(open("dog.5123.jpg"))
#img = Image.open(open("/home/hphp/Documents/code/DeepLearning/DeepLearningTutorials/doc/images/3wolfmoon.jpg"))
#img = img.resize((200,200),Image.ANTIALIAS)
#img.show()
img_w , img_h = img.size
print img.size
img = numpy.asarray(img, dtype='float64') / 256.

# put image in 4D tensor of shape (1, 3, height, width)
img_ = img.swapaxes(0, 2).swapaxes(1, 2).reshape(1, 3, img_h, img_w)
print "type of img : ", type(img) , img.shape
print "type of swapaxes(0,2):" ,type(img.swapaxes(0,2)) ,img.swapaxes(0,2).shape
print "type of swapaxes(0,2).swapaxes(1,2):" ,type(img.swapaxes(0,2).swapaxes(1,2)) ,img.swapaxes(0,2).swapaxes(1,2).shape
print "type of swapaxes(0,2).swapaxes(1,2).reshape(1,3,img_h,img_w):" ,type(img.swapaxes(0,2).swapaxes(1,2).reshape(1,3,img_h,img_w)) ,img.swapaxes(0,2).swapaxes(1,2).reshape(1,3,img_h,img_w).shape
'''
type of img :  <type 'numpy.ndarray'> (285, 304, 3)
type of swapaxes(0,2): <type 'numpy.ndarray'> (3, 304, 285)
type of swapaxes(0,2).swapaxes(1,2): <type 'numpy.ndarray'> (3, 285, 304)
type of swapaxes(0,2).swapaxes(1,2).reshape(1,3,img_h,img_w): <type
'numpy.ndarray'> (1, 3, 285, 304)
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

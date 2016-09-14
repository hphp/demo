#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2016 Baidu.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: d_image.py
Author: hanjiatong(hanjiatong@baidu.com)
Date: 2016/08/21 15:38:13
"""
import tensorflow as tf

filename_queue = tf.train.string_input_producer(['d_image.jpg']) #  list of files to read

reader = tf.WholeFileReader()
key, value = reader.read(filename_queue)

my_img = tf.image.decode_png(value) # use png or jpg decoder based on your files.
print type(my_img)
print key
print key.value

if __name__ == "__main__":
    print 'cool'
    #uint8image = tf.image.encode_jpeg("d_image.jpg")
    #print uint8image

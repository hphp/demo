#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2016 Baidu.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: basic/read_from_image_for_train.py
Author: hanjiatong(hanjiatong@baidu.com)
Date: 2016/09/11 18:18:55
"""

import tensorflow as tf

filename_queue = tf.train.string_input_producer(['sample.jpg']) #  list of files to read

reader = tf.WholeFileReader()
key, value = reader.read(filename_queue)

my_img = tf.image.decode_png(value) # use png or jpg decoder based on your files.

init_op = tf.initialize_all_variables()
with tf.Session() as sess:
  sess.run(init_op)

# Start populating the filename queue.

coord = tf.train.Coordinator()
threads = tf.train.start_queue_runners(coord=coord)

for i in range(1): #length of your filename list
  image = my_img.eval() #here is your image Tensor :) 

print(image.shape)
Image.show(Image.fromarray(np.asarray(image)))

coord.request_stop()
coord.join(threads)

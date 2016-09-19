#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2016 Baidu.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: basic/d_placeholder.py
Author: hanjiatong(hanjiatong@baidu.com)
Date: 2016/09/19 15:55:13
"""
import tensorflow as tf
import numpy as np
x = tf.placeholder(tf.float32, shape=(1024, 1024))
y = tf.matmul(x, x)

with tf.Session() as sess:
  #print(sess.run(y))  # ERROR: will fail because x was not fed.

  rand_array = np.random.rand(1024, 1024)
  first_y_value = sess.run(y, feed_dict={x: rand_array})  # Will succeed.
  print type(first_y_value) # numpy array
  print len(first_y_value)

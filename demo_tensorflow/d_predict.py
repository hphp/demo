#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2016 Baidu.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: d_predict.py
Author: hanjiatong(hanjiatong@baidu.com)
Date: 2016/07/18 11:08:30
"""
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("./data/", one_hot=True)

y = tf.placeholder(tf.float32, [None, 784])
prediciton = tf.argmax(y, 1)

session_conf = tf.ConfigProto()
sess = tf.Session(config=session_conf)
with sess.as_default():
    print prediciton.eval(feed_dict={y: mnist.test.images}, session = sess)

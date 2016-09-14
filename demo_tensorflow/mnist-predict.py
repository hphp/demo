#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2016 Baidu.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: mnist-predict.py
Author: hanjiatong(hanjiatong@baidu.com)
Date: 2016/07/18 11:34:15
"""

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

model_path = "/home/vis/hanjiatong/tensorflow/tensorflow_for_idl/demo/runs/1468813102/checkpoints/model"
#1, load in data.
mnist = input_data.read_data_sets("./data/", one_hot=True)

#2, define model 
x = tf.placeholder(tf.float32, [None, 784]) #inputs of model
W = tf.Variable(tf.zeros([784, 10])) #weights
b = tf.Variable(tf.zeros([10]))
y = tf.nn.softmax(tf.matmul(x, W) + b)#output

#3, define prediction
prediciton = tf.argmax(y, 1)

#4, restore model
saver = tf.train.Saver(tf.all_variables())
with tf.Session() as sess:
  # Restore variables from disk.
  saver.restore(sess, model_path)
  print("Model restored.")
  print prediciton.eval(feed_dict={x: mnist.test.images}, session = sess)

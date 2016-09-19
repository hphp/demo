#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2016 Baidu.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: mnist-cnn.py
Author: hanjiatong(hanjiatong@baidu.com)
Date: 2016/09/19 16:55:41
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Import data
from tensorflow.examples.tutorials.mnist import input_data

import tensorflow as tf
import numpy as np

def weight_variable(shape):
  initial = tf.truncated_normal(shape, stddev=0.1) 
    # truncated normal distribution stands for the normal distribution of which all elements lies on or above the zero line.
  return tf.Variable(initial)

def bias_variable(shape):
  initial = tf.constant(0.1, shape=shape)
  return tf.Variable(initial)

def conv2d(x, W):
  return tf.nn.conv2d(x, W\
          , strides=[1, 1, 1, 1], padding='SAME')

def max_pool_2x2(x):
  return tf.nn.max_pool(x, ksize=[1, 2, 2, 1]\
          , strides=[1, 2, 2, 1], padding='SAME')

flags = tf.app.flags
FLAGS = flags.FLAGS
flags.DEFINE_string('data_dir', '/tmp/data/', 'Directory for storing data')

#mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
mnist = input_data.read_data_sets(FLAGS.data_dir, one_hot=True)

#sess = tf.InteractiveSession()
sess = tf.Session()

# Create the model
x = tf.placeholder(tf.float32, [None, 784])
x_image = tf.reshape(x, [-1,28,28,1])
W_conv1 = weight_variable([5, 5, 1, 32])
b_conv1 = bias_variable([32])
conv_t = conv2d(x_image, W_conv1)
h_conv1 = tf.nn.relu(conv_t + b_conv1)
h_pool1 = max_pool_2x2(h_conv1)

W_conv2 = weight_variable([5, 5, 32, 64])
b_conv2 = bias_variable([64])
h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
h_pool2 = max_pool_2x2(h_conv2)

W_fc1 = weight_variable([7*7*64, 1024])
b_fc1 = bias_variable([1024])

h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64])
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

keep_prob = tf.placeholder(tf.float32)
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

W_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])
y_conv = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)

y_ = tf.placeholder(tf.float32, [None, 10])
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y_conv), reduction_indices=[1]))
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

sess.run(tf.initialize_all_variables())

# Train
#tf.initialize_all_variables().run()
for i in range(1000):
  batch_xs, batch_ys = mnist.train.next_batch(50)
  if i % 100 == 0:
      train_accuracy = accuracy.eval(feed_dict = {\
              x:batch_xs, y_:batch_ys, keep_prob:1.0 \
              }, session = sess)
      print("step:%d, training accuracy:%f" % (i, train_accuracy))
  train_step.run({x: batch_xs, y_: batch_ys, keep_prob: 0.5} \
          , session = sess)

# Test trained model
print(accuracy.eval({x: mnist.test.images, y_: mnist.test.labels}))

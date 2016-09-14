#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2016 Baidu.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: model_restore.py
Author: hanjiatong(hanjiatong@baidu.com)
Date: 2016/07/18 10:34:14
"""
import tensorflow as tf

# Create some variables.
v1 = tf.Variable(0, name="v1")
v2 = tf.Variable(0, name="v2")
# Add ops to save and restore all the variables.
saver = tf.train.Saver()

# Later, launch the model, use the saver to restore variables from disk, and
# do some work with the model.
with tf.Session() as sess:
  # Restore variables from disk.
  saver.restore(sess, "./tmp/model.ckpt")
  print("Model restored.")
  # Do some work with the model
  sess.run(at least one more argument)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2016 Baidu.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: d_tensor.py
Author: hanjiatong(hanjiatong@baidu.com)
Date: 2016/08/21 16:38:51
"""
import tensorflow as tf

a = tf.constant([1, 2])
print a
print tf.to_double(a)

b = tf.constant('b')

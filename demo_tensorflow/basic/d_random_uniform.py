#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2016 Baidu.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: basic/d_random_uniform.py
Author: hanjiatong(hanjiatong@baidu.com)
Date: 2016/09/19 14:11:12
"""
import tensorflow as tf

print tf.random_uniform([1], -1.0, 2.0) # a tensor

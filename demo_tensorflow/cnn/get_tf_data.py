#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2016 Baidu.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: get_tf_data.py
Author: hanjiatong(hanjiatong@baidu.com)
Date: 2016/08/21 17:07:36
"""

import random
import logger

import tensorflow as tf

md5_lst = []
md5_dic = {}

ran_lst = []
PARTION_SIZE = 1000

if __name__ == "__main__":
    md5_label_f = open("../data/md5_ctype", "r")
    for items in md5_label_f.readlines():
        try:
            md5, ctype = items.strip().split("\t")
            if len(md5) > 16:
                md5_lst += [md5]
                md5_dic[md5] = ctype
            elif md5 not in md5_dic:
                continue
            else:
                logger.warning("wrong length of md5ctype:%s" % items.strip())
        except:
            logger.warning("wrong formats of md5ctype:%s" % items.strip())

    random.shuffle(md5_lst)
    index = 0
    while index < len(md5_lst):
        ran_lst += [md5_lst[index: min(index+PARTION_SIZE, len(md5_lst))]]
        index += PARTION_SIZE

    print len(ran_lst)
    for ran_part in ran_lst:
        for md5 in ran_part:
            ctype = md5_dic[md5]
            key, value = tf.WholeFileReader().read(tf.train.string_input_producer([".".join(("../data/" + md5, "jpg"))]))
            tf_image = tf.image.decode_png(value) # use png or jpg decoder based on your files.

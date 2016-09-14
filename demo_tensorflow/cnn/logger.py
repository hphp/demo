#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2016 Baidu.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: logger.py
Author: hanjiatong(hanjiatong@bangdang.com)
Date: 2016/08/21 14:50:51
"""
import logging

def get_logger():

    # 创建一个logger
    logger = logging.getLogger('demo_logger')
    logger.setLevel(logging.DEBUG)

    # 创建一个handler，用于写入日志文件
    fh = logging.FileHandler('cnn.log') # default add to tail.
    fh.setLevel(logging.DEBUG)                                                                                                  
                                                                                                                                
    # 再创建一个handler，用于输出到控制台                                                                                       
    ch = logging.StreamHandler()                                                                                                
    ch.setLevel(logging.DEBUG)                                                                                                  
                                                                                                                                
    # 定义handler的输出格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')                                       
                                                                                                                                
    fh.setFormatter(formatter)                                                                                                  
    ch.setFormatter(formatter)                                                                                                  
                                                                                                                                
    # 给logger添加handler                                                                                                       
    logger.addHandler(fh)                                                                                                       
    logger.addHandler(ch)                                                                                                       
                                                                                                                                
    return logger

Logger = get_logger()

def debug(s):
    Logger.debug(s)
def info(s):
    Logger.info(s)

def warning(s):
    Logger.warning(s)

if __name__ == "__main__":
    logger = get_logger()
    logger.info('main')
    logger.debug('main')

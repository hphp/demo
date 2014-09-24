/***************************************************************************
 * 
 * Copyright (c) 2014 Baidu.com, Inc. All Rights Reserved
 * 
 **************************************************************************/
 
 
 
/**
 * @file test.cpp
 * @author hanjiatong(com@baidu.com)
 * @date 2014/06/27 19:59:47
 * @brief 
 *  
 **/
#include <unistd.h>
#include <stdio.h>
#include <errno.h>

int main(){
    int pid = fork();
    if(pid < 0){
        printf("error fork\n");
    }
    if(pid == 0){
        if(execlp("./main","main","1",NULL) < 0){
            printf("errno:%d\n",errno);
        }
    }
    else{
        printf("hello comake! I am your test child.\n");
    }
    return 0;
}





















/* vim: set expandtab ts=4 sw=4 sts=4 tw=100: */

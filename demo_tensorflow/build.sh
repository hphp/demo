#!/usr/bin

if [ "$1" == "pc" ];then
    tar czf demo_tensorflow.tar.gz *.py
    sh ~/generate_ftp_route.sh demo_tensorflow.tar.gz
elif [ "$1" == "w" ];then
    tar czf demo_tensorflow.tar.gz *
    sh ~/generate_ftp_route.sh demo_tensorflow.tar.gz
elif [ "$1" == "b" ];then
    tar czf demo_tensorflow.tar.gz basic
    sh ~/generate_ftp_route.sh demo_tensorflow.tar.gz
elif [ "$1" == "d" ];then
    wget ftp://cp01-rdqa-dev115.cp01.baidu.com//home/users/hanjiatong/svn/demo-master/demo_tensorflow/demo_tensorflow.tar.gz -O demo_tensorflow.tar.gz
    tar xzf demo_tensorflow.tar.gz
fi

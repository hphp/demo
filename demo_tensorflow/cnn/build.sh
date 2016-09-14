#!/usr/bin

if [ "$1" == "pc" ];then
    tar czf cnn.tar.gz *.py *.sh
    sh ~/generate_ftp_route.sh cnn.tar.gz
elif [ "$1" == "d" ];then
    wget ftp://cp01-rdqa-dev115.cp01.baidu.com//home/users/hanjiatong/svn/demo-master/demo_tensorflow/cnn/cnn.tar.gz -O cnn.tar.gz
    tar xzf cnn.tar.gz
fi

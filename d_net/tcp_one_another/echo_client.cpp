#include <iostream>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <sys/time.h>
#include <stdio.h>

#include "common.h"

using namespace std;

int SEND_PORT = 5566;
char SEND_IP[100] = "127.0.0.1";
int SEVR_PORT = 5567;
int PACKET_SIZE = 1024;
int PACKET_NUMBER = 10;

int main(int argsn, char ** args)
{
    if(argsn > 2 ){
        sscanf(args[1],"%d",&PACKET_SIZE);
        sscanf(args[2],"%d",&PACKET_NUMBER);
    }
    if(argsn > 4){
        sscanf(args[3],"%d",&SEND_PORT);
        sscanf(args[4],"%s",&SEND_IP);
    }
    if(argsn > 5){
        sscanf(args[5],"%d",&SEVR_PORT);
    }
    long start = gettime_usec();

    send_data(SEND_PORT,SEND_IP,PACKET_SIZE,PACKET_NUMBER);

    int sockfd ;
    listen_port(SEVR_PORT,sockfd);
    if(sockfd > 0){
        int connectfd = accept(sockfd, NULL, NULL);
        if(connectfd > 0){
            recieve_data(connectfd,PACKET_SIZE,PACKET_NUMBER);
            close(sockfd);

            long stop = gettime_usec();
            printf("%ld\n",stop-start);
        }
        else{
            printf("connect error\n");
        }
    }
    else{
        printf("listen error\n");
    }
    return 0;
}

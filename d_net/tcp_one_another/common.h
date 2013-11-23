#ifndef  _COMMON_H
#define _COMMON_H

#include <iostream>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <sys/time.h>
#include <stdio.h>
#define MAX_SIZE 10240

long gettime_usec();
void send_data(int SEND_PORT , char * SEND_IP,int MAX_MESG_SIZE, int PACKET_NUMBER);
void recieve_data(int connectfd,int MAX_MESG_SIZE , int PACKET_NUMBER );
void listen_port(int SERV_PORT,int & sockfd);

#endif

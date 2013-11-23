#include <iostream>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <sys/time.h>
#include <stdio.h>
#define SERV_PORT 5566
#define CLIENT_PORT 5567
#define MAX_MESG_SIZE 10240
#define PACKET_NUMBER 1

using namespace std;

long gettime_usec(){
    timeval tv;
    gettimeofday(&tv,NULL);
    return tv.tv_usec;
}


int main()
{
    int sockfd;
    struct sockaddr_in servaddr;
    bzero(&servaddr, sizeof(servaddr));

    servaddr.sin_family = AF_INET;
    servaddr.sin_port = htons(SERV_PORT);
    inet_aton("127.0.0.1", &servaddr.sin_addr);

    if((sockfd = socket(AF_INET, SOCK_STREAM, 0)) < 0)
    {
        printf("socket error");
        return -1;
    }
    if((connect(sockfd, (struct sockaddr*)&servaddr, sizeof(servaddr)))<0)
    {
        printf("connect error!\n");
        return -1;
    }

    char sendbuff[MAX_MESG_SIZE];
    for(int i = 0;i < MAX_MESG_SIZE ; i ++)
        sendbuff[i] = '0';
    char recvbuf[MAX_MESG_SIZE];

    long start = gettime_usec();
    int send_bytes = 0;
    int recieve_bytes = 0;
    int should_rec_bytes = PACKET_NUMBER * MAX_MESG_SIZE;
    while(send_bytes < should_rec_bytes)
    {
        ssize_t snd = send(sockfd, sendbuff, MAX_MESG_SIZE,0);
        send_bytes+= snd;
    }
    long stop = gettime_usec();
    printf("%ld\n",stop-start);
    return 0;
    while(recieve_bytes < should_rec_bytes){
        ssize_t n = recv(sockfd, recvbuf, MAX_MESG_SIZE, 0);
        recieve_bytes += n ;
    }
    //printf("%ld,%ld,",start,stop);
    stop = gettime_usec();
    printf("%ld\n",stop-start);
    return 0;
}


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
    int send_packet_num = 0;
    int recieve_packet_bytes= 0;
    int should_rec_pac_bytes = PACKET_NUMBER * MAX_MESG_SIZE;
    while(true)
    {
        int n;
        if(send_packet_num < PACKET_NUMBER){
            ssize_t snd = send(sockfd, sendbuff, MAX_MESG_SIZE,0);
        }
        if((n = recv(sockfd, recvbuf, MAX_MESG_SIZE, 0))>0)
        {
            recieve_packet_bytes += n ;
            if (recieve_packet_bytes >= should_rec_pac_bytes)
                break;
        }
        send_packet_num ++;
    }
    long stop = gettime_usec();
    //printf("%ld,%ld,",start,stop);
    printf("%ld\n",stop-start);
    return 0;
}

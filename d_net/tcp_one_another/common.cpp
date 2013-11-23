#include "common.h"


long gettime_usec(){
    timeval tv;
    gettimeofday(&tv,NULL);
    return tv.tv_usec;
}
void send_data(int SEND_PORT , char * SEND_IP,int MAX_MESG_SIZE, int PACKET_NUMBER){

    int sockfd;
    struct sockaddr_in servaddr;
    bzero(&servaddr, sizeof(servaddr));

    servaddr.sin_family = AF_INET;
    servaddr.sin_port = htons(SEND_PORT);
    inet_aton(SEND_IP, &servaddr.sin_addr);

    if((sockfd = socket(AF_INET, SOCK_STREAM, 0)) < 0)
    {
        printf("socket error");
        return ;
    }
    if((connect(sockfd, (struct sockaddr*)&servaddr, sizeof(servaddr)))<0)
    {
        printf("connect error!\n");
        return ;
    }

    char sendbuff[MAX_SIZE];
    int send_bytes = 0;
    int should_rec_bytes = PACKET_NUMBER * MAX_MESG_SIZE;
    while(send_bytes < should_rec_bytes)
    {
        ssize_t snd = send(sockfd, sendbuff, MAX_MESG_SIZE,0);
        send_bytes+= snd;
    }
    close(sockfd);
}


void listen_port(int SERV_PORT,int & sockfd){

    int connectfd;
    pid_t childpid;
    struct sockaddr_in servaddr;
    bzero(&servaddr, sizeof(servaddr));
    servaddr.sin_family = AF_INET;
    servaddr.sin_port = htons(SERV_PORT);
    servaddr.sin_addr.s_addr = htonl(INADDR_ANY);

    if((sockfd = socket(AF_INET, SOCK_STREAM, 0))<0)
    {
        printf("socket error!\n");
        return ;
    }

    if((bind(sockfd, (struct sockaddr*)&servaddr, sizeof(servaddr)))<0)
    {
        printf("bind error!\n");
        sockfd = -1;
        return ;
    }

    if(listen(sockfd, 5) < 0)
    {
        printf("listen error!\n");
        sockfd = -1;
        return ;
    }
}

void recieve_data(int connectfd,int MAX_MESG_SIZE , int PACKET_NUMBER )
{
    ssize_t n;
    char buff[MAX_SIZE];

    int rec_bytes=0;
    int should_rec = PACKET_NUMBER * MAX_MESG_SIZE;
    while((n = recv(connectfd, buff, MAX_MESG_SIZE, 0)) > 0){
        rec_bytes+=n;
        if(rec_bytes >= should_rec)
            break;
    }
    close(connectfd);
}

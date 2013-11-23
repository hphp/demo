#include <iostream>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#define SERV_PORT 5566
#define MAX_MESG_SIZE 1024
#define PACKET_NUMBER 1
using namespace std;

void recieve_data(int connectfd);
int main()
{
    int sockfd;
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
        return -1;
    }

    if((bind(sockfd, (struct sockaddr*)&servaddr, sizeof(servaddr)))<0)
    {
        printf("bind error!\n");
        return -1;
    }

    if(listen(sockfd, 5) < 0)
    {
        printf("listen error!\n");
        return -1;
    }

    while(1){
        connectfd = accept(sockfd, NULL, NULL);
        if((childpid = fork()) == 0)
        {
            close(sockfd);
            recieve_data(connectfd);
            return 0;
        }
        close(connectfd);
    }
    return 0;
}

void recieve_data(int connectfd)
{
    ssize_t n;
    char buff[MAX_MESG_SIZE];

    int rec_bytes=0;
    int should_rec = PACKET_NUMBER * MAX_MESG_SIZE;
    while((n = recv(connectfd, buff, MAX_MESG_SIZE, 0)) > 0){
        rec_bytes+=n;
        if(rec_bytes >= should_rec)
            break;
    }
    close(connectfd);
    return ;

    int send_bytes = 0;
    while(send_bytes < should_rec){
        n = send(connectfd , buff , MAX_MESG_SIZE , 0);
        send_bytes += n;
    }
    if(n < 0)
        printf("read error!\n");
}

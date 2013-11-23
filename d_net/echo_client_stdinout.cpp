#include <iostream>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#define SERV_PORT 5566
#define CLIENT_PORT 5567
#define MAX_MESG_SIZE 1024

using namespace std;

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
    char recvbuf[MAX_MESG_SIZE];
    while(fgets(sendbuff, MAX_MESG_SIZE, stdin) != NULL)
    {
        int n;
        send(sockfd, sendbuff, strlen(sendbuff), 0);
        if((n = recv(sockfd, recvbuf, MAX_MESG_SIZE, 0))>0)
        {
            recvbuf[n] = 0;
            fputs(recvbuf, stdout);
        }
    }
    return 0;
}

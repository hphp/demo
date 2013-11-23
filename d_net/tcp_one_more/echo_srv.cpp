#include <iostream>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#define SERV_PORT 5566
#define MAX_MESG_SIZE 10240
using namespace std;

void my_echo(int connectfd);
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

    while(1)
    {
        connectfd = accept(sockfd, NULL, NULL);
        if((childpid = fork()) == 0)
        {
            close(sockfd);
            my_echo(connectfd);
            return 0;
        }
        close(connectfd);
    }
    return 0;
}

void my_echo(int connectfd)
{
    ssize_t n;
    char buff[MAX_MESG_SIZE];

    int rc_n = 0;
    int should_recieve = 10240;
    while(true){
        int n;
        if((n = recv(connectfd, buff, MAX_MESG_SIZE + 1, 0)) > 0)
            rc_n += n;
        if(n < 0)
            printf("read error!\n");
        if(rc_n >= should_recieve)
            break;
        printf("%d\n",rc_n);
    }
    printf("have read %d\n",should_recieve);
    send(connectfd, buff, should_recieve, 0);
}

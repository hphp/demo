#include <iostream>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <sys/wait.h>
#include <arpa/inet.h>
#include <stdlib.h>
#define MAX_MESG_SIZE 1024
#include <sys/select.h>
#include <sys/time.h>
using namespace std;

void my_echo(int connectfd);
long gettime_usec(){
    timeval tv;
    gettimeofday(&tv,NULL);
    return tv.tv_usec;
}

int PACKET_SIZE = 512;
int PACKET_NUMBER = 10;
int SERV_PORT = 5566;
int SUM = 10;

int main(int argsn, char **args)
{
	if(argsn > 1){
		sscanf(args[1],"%d",&SERV_PORT);
	}

    int sockfd;
    int connectfd;
    pid_t childpid;
    struct sockaddr_in servaddr;

    if((sockfd = socket(AF_INET, SOCK_STREAM, 0))<0)
    {
        printf("socket error! %d\n",errno);
        return -1;
    }

    int on = 1;
    int ret = setsockopt( sockfd, SOL_SOCKET, SO_REUSEADDR, &on, sizeof(on) );
    /* Allow connections to some port from any available interface */
    //   printf("%d %d\n",ret,errno);


    bzero(&servaddr, sizeof(servaddr));
    servaddr.sin_family = AF_INET;
    servaddr.sin_port = htons(SERV_PORT);
    inet_aton("172.27.200.198",&servaddr.sin_addr);
    //servaddr.sin_addr.s_addr = htonl(INADDR_ANY);

    if((bind(sockfd, (struct sockaddr*)&servaddr, sizeof(servaddr)))<0)
    {
        printf("bind error! %d\n",errno);
        return -1;
    }

    if(listen(sockfd, 5) < 0)
    {
        printf("listen error!\n");
        return -1;
    }

    int sum =0;
    while(1){
	    connectfd = accept(sockfd, NULL, NULL);
	    if(connectfd > 0){
		    my_echo(connectfd);
		    close(connectfd);
	    }
    }
    return 0;
}

void my_echo(int connectfd)
{
	ssize_t n;
	char buff[2<<20];

	int rc_n = 0;
	int sum = 0;
	long sec = 0, usec = 0;
	while(true){
		int n;
		if((n = recv(connectfd, buff, 2<<12, 0)) > 0) {
			if (rc_n == 0) {
				sscanf(buff,"%ld,%ld",&sec,&usec);
			}
			rc_n += n;
		} else {
			timeval tv;
			gettimeofday(&tv,NULL);
			printf("%d\t%ld\n", rc_n, (tv.tv_sec - sec) * 1000000 + tv.tv_usec - usec);
			fflush(stdout);
			close(connectfd);break;
		}
	}
	//	close(connectfd);
}

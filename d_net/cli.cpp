#include <iostream>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <sys/time.h>
#include <stdio.h>
#include <string.h>
#include <errno.h>

#include <sys/select.h>
#define MAX_MESG_SIZE 2097153

using namespace std;

long gettime_usec(){
	timeval tv;
	gettimeofday(&tv,NULL);
	return tv.tv_usec;
}

int PACKET_SIZE = 512;
int PACKET_NUMBER = 10;
int SEND_PORT = 5566;
char SEND_IP[20] = "127.0.0.1";
int SERV_PORT = 5567;
int SUM = 10;

int sockfd;
struct sockaddr_in servaddr;

void get_socket(){

	bzero(&servaddr, sizeof(servaddr));

	servaddr.sin_family = AF_INET;
	servaddr.sin_port = htons(SEND_PORT);
	inet_aton(SEND_IP , &servaddr.sin_addr);

	if((sockfd = socket(AF_INET, SOCK_STREAM, 0)) < 0)
	{
		perror("socket error");
	}
	if((connect(sockfd, (struct sockaddr*)&servaddr, sizeof(servaddr)))<0)
	{
		perror("connect error!\n");
	}
}

char sendbuff[MAX_MESG_SIZE];

int main(int argsn, char ** args)
{
	if(argsn > 2 ){
		sscanf(args[1],"%d",&PACKET_SIZE);
		sscanf(args[2],"%d",&PACKET_NUMBER);
	}
	if(argsn > 4){
		sscanf(args[3],"%d",&SEND_PORT);
		sscanf(args[4],"%s",SEND_IP);
	}
	PACKET_SIZE = PACKET_SIZE * 1024;
	for (int i = 0; i < PACKET_NUMBER; i++) {

		get_socket();
		printf("get conn\n");

		timeval tv_start;
		gettimeofday(&tv_start,NULL);
		sprintf(sendbuff,"%ld,%ld",tv_start.tv_sec,tv_start.tv_usec);
		int send_size = 0;
		while(true){

			ssize_t snd = send(sockfd, sendbuff, PACKET_SIZE - send_size,0);
			if(snd >= 0)send_size += snd;
			else {perror("send error."); break;}
			printf("sent %d\n", send_size);
			if(send_size >= PACKET_SIZE){
				close(sockfd); break;
				printf("closed\n");
			}
		}
	}
	return 0;
}

#include <iostream>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#define SERV_PORT 5566
#define MAX_MESG_SIZE 1024
#define PACKET_NUMBER 10
using namespace std;

void dg_echo(int sockfd ,struct sockaddr *pcliaddr,socklen_t clilen);

int main(int argc, char **argv)
{
	int sockfd;

	struct sockaddr_in	cliaddr, servaddr;

	sockfd = socket(AF_INET, SOCK_DGRAM, 0);

	bzero(&servaddr, sizeof(servaddr));
	servaddr.sin_family      = AF_INET;
	servaddr.sin_addr.s_addr = htonl(INADDR_ANY);
	servaddr.sin_port        = htons(SERV_PORT);

	bind(sockfd, (struct sockaddr *) &servaddr, sizeof(servaddr));

    dg_echo(sockfd,(struct sockaddr* ) &cliaddr, sizeof(cliaddr));

    close(sockfd);

}

void dg_echo(int sockfd ,struct sockaddr *pcliaddr,socklen_t clilen)
{
    int n;
    socklen_t len;
    char mesg[MAX_MESG_SIZE];

    int pckt_nmbr = 0;
    for( ; ;)
    {
        len = clilen;
        n = recvfrom(sockfd, mesg, MAX_MESG_SIZE,0 ,pcliaddr,&len);
        printf("%d\n",n);
        pckt_nmbr ++;
        if(pckt_nmbr >= PACKET_NUMBER)
            break;
        // here what if the recieved n is smaller than the defined number ?
//        sendto(sockfd,mesg,n, 0, pcliaddr ,len);
    }
}

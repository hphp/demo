#include <iostream>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <sys/time.h>
#define SERV_PORT 5566
#define MAX_MESG_SIZE 1024
#define DEST_IP "127.0.0.1"
#define PACKET_NUMBER 10
using namespace std;

void dg_cli(FILE *fp, int sockfd, const struct sockaddr* pservaddr, socklen_t servlen);

int main(int argc, char ** argv)
{
    int sockfd;

    struct sockaddr_in servaddr;

    sockfd = socket(AF_INET, SOCK_DGRAM, 0);

    bzero(&servaddr, sizeof(struct sockaddr_in));
    servaddr.sin_family = AF_INET;
    servaddr.sin_port = htons(SERV_PORT);

    inet_pton(AF_INET, DEST_IP, &servaddr.sin_addr);

    dg_cli(stdin, sockfd, (struct sockaddr *) &servaddr ,sizeof(servaddr));
    exit(0);
}

/*
void dg_cli(FILE *fp, int sockfd, const struct sockaddr* pservaddr, socklen_t servlen)
{
    int     n;
    char    sendline[MAX_MESG_SIZE], recvline[MAX_MESG_SIZE+1];
    while(Fgets(sendline, MAX_MESG_SIZE, fp) != NULL)
    {
        Sendto(sockfd, sendline, strlen(sendline), 0 , pservaddr, servlen);

        n = Recvfrom(sockfd ,recvline, MAX_MESG_SIZE, 0, NULL, NULL);

        recvline[n] = 0;

        Fputs(recvline, stdout);
    }
}
#include "unp.h"
*/

long gettime_usec(){
    timeval tv;
    gettimeofday(&tv,NULL);
    return tv.tv_usec;
}

void dg_cli(FILE *fp, int sockfd, const struct sockaddr* pservaddr, socklen_t servlen)
{
    int n;
    char sendline[MAX_MESG_SIZE], recvline[MAX_MESG_SIZE+1];
    socklen_t len;
    struct sockaddr *preply_addr;
    preply_addr = (struct sockaddr*)malloc(servlen);

    long start = gettime_usec();
    int send_packet_num = 0;
    int recieve_packet_bytes= 0;
    int should_rec_pac_bytes = PACKET_NUMBER * MAX_MESG_SIZE;
    while(true)
    {
        if(send_packet_num < PACKET_NUMBER){
            sendto(sockfd, sendline, MAX_MESG_SIZE, 0 , pservaddr, servlen);
        }

        send_packet_num ++;
    }
/*
    while(true){

        len  = servlen;

        n = recvfrom(sockfd ,recvline, MAX_MESG_SIZE, 0, preply_addr, &len);

        if(len != servlen || memcmp(pservaddr, preply_addr, len) != 0)
        {
            //printf("reply from (ignored)\n");//, sock_ntop(preply_addr, len));
            continue;
        }


        recieve_packet_bytes += n ;
        if (recieve_packet_bytes >= should_rec_pac_bytes)
            break;
    }
    */
    free(preply_addr);
    long stop = gettime_usec();
    //printf("%ld,%ld,",start,stop);
    printf("%ld\n",stop-start);
}

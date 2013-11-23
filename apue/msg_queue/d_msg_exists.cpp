
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/msg.h>
#include <string.h>
#include <sys/ipc.h>
#include <map>
#include <string>
#include <algorithm>
using namespace std;
#define ROUTE_LENGTH 512
#define MSG_LENGTH 1024
#define MAX_PERIOD 10800
char PRJ_PATH[512];
int PRJ_ID;

void get_config(){
	FILE * f = fopen("../dlspt.conf","r");
	if(f != NULL){
		char read_in[512] = "";
		while(fgets(read_in,ROUTE_LENGTH,f) != NULL){
			char a[ROUTE_LENGTH],b[ROUTE_LENGTH],c[ROUTE_LENGTH];
			sscanf(read_in,"%s%s%s",a,b,c);
			if(strcmp(a,"PRJ_PATH") == 0){
				strcpy(PRJ_PATH,c);
			}
			else if(strcmp(a,"PRJ_ID") == 0){
				sscanf(c,"%d",&PRJ_ID);
			}
		}
	}
	printf("prj_path:%s,prj_id:%d\n",PRJ_PATH,PRJ_ID);
}

int main(){
	get_config();
	int flag = IPC_CREAT|IPC_EXCL;
	key_t msg_key = ftok(PRJ_PATH,PRJ_ID);
	int msgqid = msgget(msg_key,flag);
	printf("%d\n",msgqid);
	if(msgqid < 0){
		msgqid=msgget(msg_key,0);
		printf("second:%d\n",msgqid);
		if(errno == EEXIST){
			if(msgctl(msgqid,IPC_RMID,NULL)!=0){
				printf("msgctl error\n");
			}
			else{
				msgqid=msgget(msg_key,flag);
				if(msgqid > 0){
					printf("good,%d\n",msgqid);
				}
				else return 0;
			}
		}
		else{
			printf("%d\n",msgqid);
		}
		return 0;
	}

	flag = 0;
	while(true){
		char ptr[MSG_LENGTH];
		long type = 0;
		ssize_t rcv_length = msgrcv(msgqid,ptr,MSG_LENGTH,type,flag);
		if(rcv_length == strlen(ptr)){
			printf("hey,i've get msg:%d,%s\n",rcv_length,ptr);
		}
		else{
			if(rcv_length < 0)
			{
				printf("oh , no , error\n");break;
			}
			printf("hey , i've get different size of msg for msglength:%d,and msg:%s\n",rcv_length,ptr);
		}
	}
	return 0;
}

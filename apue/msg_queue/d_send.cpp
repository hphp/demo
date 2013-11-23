#include <stdio.h>
#include <sys/msg.h>
#include <string.h>
#include <string>
using namespace std;
#define P_TYPE_LENGTH 512
#define P_MSG_LENGTH 512
#define ROUTE_LENGTH 512

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
	int msgqid = 0;
	char p_type[P_TYPE_LENGTH],p_msg[P_MSG_LENGTH],p_occurence_time[P_MSG_LENGTH];
	scanf("%s%s%s",p_type,p_occurence_time,p_msg);

	char ptr[P_MSG_LENGTH];
	strcpy(ptr,p_msg);


	int flag = 0;
        key_t msg_key = ftok(PRJ_PATH,PRJ_ID);
        printf("%d\n",msg_key);

        msgqid = msgget(msg_key,flag);
	printf("get_msgqid %d\n",msgqid);

	if (msgqid < 0){
		printf("sorry , cant find such msg queue , msgqid %d\n",msgqid);
		return 0;
	}
	string send = "";
	send += p_type;
	send += ",";
	send += p_occurence_time;
	send += ",";
	send += p_msg;
	printf("will send %s,%d\n",send.c_str(),send.length());
	int rc_snd = msgsnd(msgqid,send.c_str(),send.length(),IPC_NOWAIT);
	if(rc_snd < 0){
		printf("hey , u've send a msg failed\n");
	}
}

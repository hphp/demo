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

struct WList;
struct WList{
	int occurence_time;
	WList * next;
};

struct WARNING_INFO{
	string warn_type;
	string warn_info;
	int limit_occurence_number;
	int limit_occurence_period;
	int warn_period;
	int last_warn_time;
	WList * head;
	WList * tail;
};
map<string,WARNING_INFO> mm;
map<string,WARNING_INFO>::iterator mit;

void new_warn_info(string warn_type,string warn_info,int o_time){
	int limit_occurence_number = 0;
	int limit_occurence_period = 0;
	int warn_period = MAX_PERIOD;
	int last_warn_time = 0;
//	FILE * f = fopen("/usr/local/dl_support/dlspt.conf","r");
	FILE * f = fopen("../dlspt.conf","r");
	if( f == NULL){
		printf("oh no , we cant open /usr/local/dl_support/dlspt.conf");
	}
	else{
		char line[1000];
		while(fgets(line,1000,f) != NULL){
			char a[1000],b[1000];
			sscanf(line,"%s = %s",a,b);
			string t_type=warn_type;
			t_type += "_LIMIT_OCCURENCE_NUMBER";
			if (strcmp(t_type.c_str(),a) == 0){
				sscanf(b,"%d",&limit_occurence_number);
			}
			t_type = warn_type;	
			t_type += "_LIMIT_OCCURENCE_PERIOD";
			if (strcmp(t_type.c_str(),a) == 0){
				sscanf(b,"%d",&limit_occurence_period);
			}
			t_type = warn_type;	
			t_type += "_WARN_PERIOD";
			if (strcmp(t_type.c_str(),a) == 0){
				sscanf(b,"%d",&warn_period);
			}
		}
		WList * tail = (WList *)malloc(sizeof(WList));
		WList * head = tail;
		tail->occurence_time = 0;
		tail->next=NULL;
		for(int i = 1 ; i < limit_occurence_number ; i ++){
			WList * cur = (WList*)malloc(sizeof(WList));
			cur->occurence_time=0;
			cur->next=NULL;
			tail->next = cur;
			tail = cur;
		}
		tail->next = head;

		WARNING_INFO wi = {warn_type,warn_info,limit_occurence_number,limit_occurence_period,warn_period,last_warn_time,head,tail};
		mm.insert( pair<string,WARNING_INFO>(warn_type , wi));

		fclose(f);
	}
}

void set_warn_info(string warn_type,string warn_info,int o_time){
	mit = mm.find(warn_type);
	if(mit == mm.end()){
		new_warn_info(warn_type,warn_info,o_time);
		mit = mm.find(warn_type);
		if(mit == mm.end()){
			printf(" insert fail or find failure.\n");
		}
	}

	WList * head = NULL , * tail = NULL;
	WARNING_INFO wi = mit->second;
	head = (mit->second).head;
	tail = (mit->second).tail;
	head->occurence_time = o_time;
	tail = head;
	head = head->next;
	int d_value = (tail->occurence_time) - (head->occurence_time);
	if (d_value < (wi.limit_occurence_period)){
		if(o_time - wi.last_warn_time > wi.warn_period){
			char cmd[10000];
			sprintf(cmd,"/usr/local/agenttools/agent/agentRepStr 200931 \"%s,%s\"",warn_type.c_str(),warn_info.c_str());
			if(system(cmd) != 0){
				printf("cmd run failure , cmd:%s\n",cmd);
				(mit->second).last_warn_time = o_time;
			}
		}
	}

	(mit->second).head = head;
	(mit->second).tail = tail;
/*
	for(head = (mit->second).head; head != (mit->second).tail ; head = head->next){
		printf("%d %s\n",head->occurence_time,(mit->second).warn_info.c_str());
	}
	printf("%d %s\n",head->occurence_time,(mit->second).warn_info.c_str());
*/
}

void get_warn_info(char * ptr,string &warn_type,int & occurence_time,string & warn_info){
	char t[MSG_LENGTH],info[MSG_LENGTH];
	sscanf(ptr,"%[^,],%d,%[^,]",t,&occurence_time,info);
	warn_type=t;
	warn_info=info;
}

int main(){
	get_config();
	int flag = IPC_CREAT ;
	key_t msg_key = ftok(PRJ_PATH,PRJ_ID);
	printf("msg_key %d\n",msg_key);
	
	int msgqid = msgget(msg_key,flag);
	if(msgqid < 0){
		printf("excuse me , we cant get exact msgqid with return code:%d\n",msgqid);
		return 0;
	}
	printf("msgqid %d\n",msgqid);
	flag = 0;
	while(true){
		char ptr[MSG_LENGTH];
		long type = 0;
		ssize_t rcv_length = msgrcv(msgqid,ptr,MSG_LENGTH,type,flag);
		if(rcv_length == strlen(ptr)){
			printf("hey,i've get msg:%d,%s\n",rcv_length,ptr);
			string warn_type,warn_info;
			int occurence_time;
			get_warn_info(ptr,warn_type,occurence_time,warn_info);
			set_warn_info(warn_type,warn_info,occurence_time);
		}
		else{
			if(rcv_length < 0)
				break;
			printf("hey , i've get different size of msg for msglength:%d,and msg:%s\n",rcv_length,ptr);
		}
	}
	return 0;
}

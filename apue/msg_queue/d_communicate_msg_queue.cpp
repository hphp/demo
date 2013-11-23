#include <sys/msg.h>
#include <stdio.h>
#include <string.h>

int main(){
	int flag = 0;
	int msgqid = msgget(IPC_PRIVATE,flag);
	printf("%d\n",msgqid);

	char ptr[1000] = "abcdefg";
	int send = msgsnd(msgqid,ptr,strlen(ptr),flag);
	printf("%d\n",send);


	ssize_t msg_rcv=0;
/*
	msg_rcv = msgrcv(msgqid,ptr,BUFSIZ,0,flag);
	printf("%d,%s\n",msg_rcv,ptr);
*/
	strcpy(ptr,"1234567890");

	send = msgsnd(msgqid,ptr,strlen(ptr),flag);
	printf("%d\n",send);
	
	while (true){
		msqid_ds buf;
		int ctl = msgctl(msgqid,IPC_STAT,&buf);
		printf("ctlreturn:%d,size:%d\n",ctl,buf.msg_qnum);
		msg_rcv = msgrcv(msgqid,ptr,BUFSIZ,0,flag);
		if(msg_rcv > 0)
			printf("%d,%s\n",msg_rcv,ptr);
		//if(buf.msg_qnum == 0)break;
	}
	
	return 0;
}

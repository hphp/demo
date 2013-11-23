#include <stdio.h>
#include <sys/msg.h>
#include <string.h>
int main(){
	int msgqid = 0;
	scanf("%d",&msgqid);
	char a[10000];
	while(scanf("%s",a)!=EOF){
		int flag = 0;
		int rc = msgsnd(msgqid,a,strlen(a),flag);
		printf("%d\n",rc);
	}
	return 0;
}

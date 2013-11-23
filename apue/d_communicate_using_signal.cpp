#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <string.h>
#include <unistd.h>
char s[1000]="good\n";
void sigusr1(int signo){
	if(signo == SIGUSR1){
		//printf("catch sigusr1 success\n");
		strcpy(s,"after catch\n");
		printf("%s\n",s);
//		system("echo good");
	}
	else{
		printf("catch wrong with %d\n",signo);
	}
}

void basic_test(){

	int returnc=setvbuf(stdout,NULL,_IOLBF,BUFSIZ);
	printf("%d\n",returnc);
	printf("hi\n");
	while(true){
		if(signal(SIGUSR1,sigusr1)==SIG_ERR){
			printf("catch failure\n");
			sleep(2);
		}
		sleep(1);
	}
}

int main(){
//	system("echo 'lets start'");
	if(signal(SIGUSR1,sigusr1)==SIG_ERR){
		printf("catch failure\n");
	}
	int a;
	while(scanf("%d",&a)!=EOF){
		printf("%d\n",a);
	}
	return 0;
}

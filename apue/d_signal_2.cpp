#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <string.h>
#include <unistd.h>
char s[1000]="good\n";
void sigusr1(int signo){
	if(signo == SIGUSR1){
		printf("catch sigusr1 success\n");
		strcpy(s,"after catch\n");
	}
	else{
		printf("catch wrong with %d\n",signo);
	}
}

int main(){
	while(true){
		if(signal(SIGUSR1,sigusr1)==SIG_ERR){
			printf("catch failure\n");
			sleep(2);
		}
		printf("%s",s);
		sleep(1);
	}
	return 0;
}

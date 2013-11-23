#include <stdio.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>
int main(){
	int fd[2];
	int rc = pipe(fd);
	if(rc == 0){
		int pid;
		if((pid = fork()) < 0){
			printf("fork err %d\n",errno);
		}
		else if( pid == 0 ){
			char s[10000];
			close(fd[1]);
			while(1){
				read(fd[0],s,10000);
				sleep(5);
				write(STDOUT_FILENO,s,strlen(s));
			}
		}
		else{
			char s[10000];
			for(int i = 0 ;i < 4095 ; i ++){
				s[i]='a';
			}
			s[4095]='\0';
			close(fd[0]);
			int a = 0;
			while(1){
				write(fd[1],s,strlen(s));
				char x[10];
				sprintf(x,"%d,",a++);
				write(STDOUT_FILENO,x,strlen(x));
			}
		}
	}
	else{
		printf("%d\n",errno);
	}
	return 0;
}

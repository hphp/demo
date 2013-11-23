#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/select.h>

fd_set * fdsetr = (fd_set*)malloc(sizeof(fdsetr));


int main(){
	//setbuf(STDIN_FILENO,NULL);
	char s[100];
	timeval tv={0,1};
	while(1)
	{
		FD_ZERO(fdsetr);
		FD_SET(STDIN_FILENO,fdsetr);
		if(select(STDIN_FILENO+1,fdsetr,NULL,NULL,&tv)==1){
			read(STDIN_FILENO,s,100);
			printf("%s\n",s);
		}
		sleep(5);
	}
	return 0;
}

#include <stdio.h>
#include <errno.h>
#include <fcntl.h>
#include <unistd.h>

int main(){
	int fd[2];
	int size = 4096;
	if(pipe(fd) == 0){
		fcntl(fd[1],F_SETPIPE_SZ,size);
	}
	else{
		printf("pipe err , errno %d\n",errno);
	}
	return 0;
}

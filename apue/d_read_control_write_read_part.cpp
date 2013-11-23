#include <stdio.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>
/*
	when write to pipe buffer each time , the read blocking status may show in effects.
*/

char s[100000];
int main(){
/*
	int fd = mkfifo("d_read_control_write.pipe",O_RDONLY);
	if(fd < 0){
		printf("mkfifo error %d, errno:%d\n",fd,errno);
	}
*/
	long pipe_buf_size = fpathconf(STDOUT_FILENO,_PC_PIPE_BUF);
	printf("%ld\n",pipe_buf_size);
	int a= 0;
	int b=0;
	while(1){
		if((b=read(STDIN_FILENO,s,pipe_buf_size*100)) <= 0)break;
		//write(STDOUT_FILENO,s,strlen(s));
		printf("%d,%d,%s\n",b,a,s);
		sleep(10);
		a++;
	}
	return 0;	
}

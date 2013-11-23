#include <stdio.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>
#include <unistd.h>
/*
	when write to pipe buffer each time , the read blocking status may show in effects.
*/

char s[100000];
int main(){
/*
	int fd = mkfifo("d_read_control_write.pipe",O_WRONLY);
	if(fd < 0){
		printf("mkfifo error %d, errno:%d\n",fd,errno);
	}
*/
	int fd = open("d_read_control_write.out",O_WRONLY|O_CREAT);
	long pipe_buf_size = fpathconf(STDOUT_FILENO,_PC_PIPE_BUF);
	//printf("%ld\n",pipe_buf_size);
	for(int i = 0 ;i < pipe_buf_size-2 ; i ++){
		s[i]='a';
	}
	s[pipe_buf_size-1]='\0';
	int a =0;
	while(1){
		write(STDOUT_FILENO,s,strlen(s));
		//fsync(STDOUT_FILENO);
		char x[10]="";
		sprintf(x,"%d",a);
		a++;
		write(fd,x,strlen(x));
		//fsync(fd);
	}
	return 0;	
}

#include <stdio.h>
#include <sys/stat.h>
#include <unistd.h>
#include <fcntl.h>
#include <errno.h>

int main(){
	int fd=mkfifo("xa",O_RDONLY);
	printf("%d\n",fd);
	if(fd < 0){
		printf("mkfifo fail , errno %d\n",errno);
	}
	long rc = fpathconf(fd , _PC_PIPE_BUF);
	printf("%ld\n",rc);
	close(fd);
	return 0;
}

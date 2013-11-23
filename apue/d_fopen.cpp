#include <stdio.h>
#include <unistd.h>
#include <errno.h>
#include <fcntl.h>

int main(){
//	int fd = open("/data/xx/xx/xx",O_CREAT|O_RDONLY);// cant create a file
	int fd = open("/data/xx/xx/xx",O_CREAT|O_RDONLY, S_IRUSR | S_IRGRP | S_IROTH
);
	if(fd <= 0)
	{
		printf("errno:open%d\n",errno);
	}
	printf("%d\n",fd);
	FILE * a = fopen("/data/xx/xx/xx","a+");
	if(a == NULL){
		printf("errno:%d\n",errno);
	}
	return 0;
}

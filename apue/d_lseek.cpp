#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <errno.h>
char buf[100];
int whole_bytes=0;

struct stat st;


/*

offset is for ur currently open file.

for a opened file , with fd , if stat it at diff time , stat results could be different
and , when u wanna reread file when it is growing or changing , a stupid silly way is to record what u have read yet.

, after a read function , the offset of a file added the number of bytes u've read. 

*/

void basic_test(){

	int b = 0;
	while(b < 20){
		int fd = open("d_lseek.in",O_RDONLY);
		lseek(fd,whole_bytes,SEEK_SET);
		if(fstat(fd,&st) < 0)
			printf("errno%d\n",errno);
		printf("\nbytes:%d,whole:%d\n",st.st_size,whole_bytes);
		int a = 0;
		while(true){
		//while(a < 20){
			off_t cur = lseek(fd,0,SEEK_CUR);
			printf("offset before:%d,",cur);
			int n = read(fd,buf,20);
			cur = lseek(fd,0,SEEK_CUR);
			printf("offset after:%d,have read:%d\n",cur,n);
			if(n <= 0)break;
			printf("%s",buf);
			a++;
			sleep(2);
			whole_bytes+=n;
		}
		if(fstat(fd,&st) < 0)
			printf("errno%d\n",errno);
		printf("\nbytes:%d,whole:%d\n",st.st_size,whole_bytes);
		//whole_bytes=st.st_size;
		sleep(2);
		close(fd);
		b++;
	}
}

int main(){
	//int fd = open("d_lseek.in",O_WRONLY|O_APPEND);
	int fd = open("d_lseek.in",O_RDONLY);
	off_t cur ;
	cur = lseek(fd,0,SEEK_END);
	printf("fd:%d,%zu,\n",fd,cur);
	cur = lseek(fd,0,SEEK_CUR);
	printf("fd:%d,%zu,\n",fd,cur);
	cur = lseek(fd,0,SEEK_END);
	printf("fd:%d,%zu,\n",fd,cur);
	return 0;	
}

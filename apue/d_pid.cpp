#include <unistd.h>
#include <stdio.h>
#include <sys/wait.h>

pid_t gid=0;

int main(){
	printf("%zu\n",getpid());
	gid = getpid();
	int a;
	int cnt = 0;
	while(cnt ++ < 2 ){
		pid_t px = fork();
		if(px < 0){
			
		}
		else if(px == 0){
			printf("i'm son:my pid:%d,gid:%d,my gidrc:%zu,mygid:%d\n",getpid(),gid,setpgid(getpid(),gid),getpgid(0));
			printf("i,m over%d\n",getpid());
			execlp("./d_pid_write.sh","./d_pid_write.sh",NULL);
		}
		else{
			printf("i'm father:my pid:%d,gid:%d,my gidrc:%zu,mygid:%d\n",getpid(),gid,setpgid(getpid(),gid),getpgid(0));
			printf("i,m over%d\n",getpid());
			sleep(4);
			int statloc;
			for(int i =0 ; i <= cnt ;i ++){
				pid_t son_pid = waitpid(0,&statloc,WNOHANG);
				printf("here's a son:%d\n",son_pid);
			}
		}	
	}
	return 0;
}

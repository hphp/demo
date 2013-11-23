#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/select.h>
#include <sys/wait.h>

/*
   test if dont wait select and pid ,what behaviour does this process occupy cpu . 
	and ,as the test results. cpu just lay at 10-15%
*/

int number = 0;

pid_t g_pgid=0;

int can_read(){
	timeval tv = {0,50000};
	fd_set rfds;
	FD_ZERO(&rfds);
	FD_SET(STDIN_FILENO,&rfds);
	if(select(STDIN_FILENO+1,&rfds,NULL,NULL,&tv) > 0){
		char line[100];
		fgets(line,100,stdin);
		//printf(".%s,",line);
		pid_t pid = fork();
		if(pid == 0){
			setpgid(getpid(),g_pgid);
			//printf("hey,i'm son\n");
			execlp("./d_select_waitpid.sh","./d_select_waitpid.sh",NULL);
			exit(0);
		}
		else{
			//printf("myson:%zu\n",pid);
			number++;
		}
		return 1;
	}
	else return 0;
}

int main(){

        g_pgid=getpid();
	setpgid(g_pgid,g_pgid);
	while(true){
		int i = number;
		while(i < 50 && number < 50){
			if(can_read()){

			}
			else break;
			i++;
		}
		while(number >= 0){
			int statloc;
			pid_t s_pid = waitpid(0,&statloc,WNOHANG);
			if(s_pid > 0){
				number--;
				//printf("hey , my son%zu, has exit\n",s_pid);
			}
			else break;
		}
	}
	return 0;
}

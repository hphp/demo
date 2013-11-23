#include <sys/select.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <string.h>
#include <signal.h>
int fd[2];
fd_set *fdsetr = (fd_set*)malloc(sizeof(fd_set));
fd_set *fdsetw = (fd_set*)malloc(sizeof(fd_set));
fd_set *fdsete = (fd_set*)malloc(sizeof(fd_set));

void non_block_select_waiting_basic(){
        FD_SET(fd[0],fdsetr);
        FD_SET(fd[1],fdsetw);
        FD_SET(STDOUT_FILENO,fdsete);

        int pid=fork();
        if(pid < 0){
            printf("fork error\n");
        }
        else if(pid == 0){
            close(fd[0]);
            sleep(2);
            timeval *tvptr = (timeval*)malloc(sizeof(timeval));
            tvptr->tv_sec=1;
            tvptr->tv_usec=0;
            int r= select(3,fdsetr,fdsetw,fdsete,tvptr);
            printf("%d\n",r);
            printf("%d\n",FD_ISSET(fd[0],fdsetr));// 0 
            printf("%d\n",FD_ISSET(fd[1],fdsetw));// 0
            printf("%d\n",FD_ISSET(STDOUT_FILENO,fdsete));// 0 
            printf("hey , fd0 is ready to read as well as for me to write\n");
            write(fd[1],"hi,i am here again\n",25);
        }
        else if(pid > 0){
            close(fd[1]);
            char line[1000]="";
            int n = read(fd[0],line,1000);
            write(STDOUT_FILENO,line,40);
        }
}
void non_block_select_basic_try1(){
        FD_SET(fd[0],fdsetr);
        FD_SET(fd[1],fdsetw);
        FD_SET(STDOUT_FILENO,fdsete);

    timeval *tvptr = (timeval*)malloc(sizeof(timeval));
    tvptr->tv_sec=0;
    tvptr->tv_usec=0;
    int r=select(3,fdsetr,fdsetw,fdsete,tvptr);
    printf("r\n");// output 0
    printf("%d\n",FD_ISSET(fd[0],fdsetr));// 0 
    printf("%d\n",FD_ISSET(fd[1],fdsetw));// 0
    int pid=fork();
    if(pid < 0){
        printf("fork error\n");
    }
    else if(pid == 0){
        close(fd[0]);
        printf("%d\n",r);
        printf("%d\n",FD_ISSET(fd[0],fdsetr));// 0
        write(fd[1],"hi,i am here again\n",35);
        /*
           if(FD_ISSET(fd[0],fdsetr)){
           printf("hey , fd0 is ready to read as well as for me to write\n");
           write(fd[1],"hi,i am here again\n",25);
           }
           else{
           printf("hey , fd0 is not ready for me to read\n");
           }
        //select() 
        */
    }
    else if(pid > 0){
        close(fd[1]);
        char line[1000]="";
        int n = read(fd[0],line,1000);
        write(STDOUT_FILENO,line,20);
    }
}

int max(int a,int b){
    return a>b?a:b;
}

void whole_block_select_basic_try3(){
    close(fd[0]);
    close(fd[1]);

    int a;
    pid_t pid = fork();
    if(pid < 0)printf("fork error\n");
    else if (pid == 0){
        while(scanf("%d",&a)!=EOF){
            printf("hey , i am pfather %d\n",a);
            sleep(1);
            FD_ZERO(fdsetr);
            FD_ZERO(fdsetw);
            FD_ZERO(fdsete);
            fd[1]=open("tmp",O_WRONLY);
            FD_SET(fd[1],fdsetw);
            int r=select(max(fd[0],fd[1])+1,fdsetr,fdsetw,fdsete,NULL);
            /*
               printf("%d\n",r);// output 0
               printf("%d\n",FD_ISSET(fd[0],fdsetr));// 0 
               printf("%d\n",FD_ISSET(fd[1],fdsetw));// 0
               */
            if(FD_ISSET(fd[1],fdsetw)){
                char line[100]="";
                sprintf(line,"i can write a = %d\n",a);
                write(fd[1],line,strlen(line));
            }
            close(fd[1]);
        }
    }
    else if(pid > 0){
        printf("hey , i am pson with pid %d\n",pid);
        FD_ZERO(fdsetr);
        FD_ZERO(fdsetw);
        FD_ZERO(fdsete);
        fd[0]=open("tmp",O_RDONLY);
        FD_SET(fd[0],fdsetr);
        int r = -1;
        while (r=select(max(fd[0],fd[1])+1,fdsetr,NULL,fdsete,NULL) != -2){
            /*
               printf("%d\n",r);// output 0
               printf("%d\n",FD_ISSET(fd[0],fdsetr));// 0 
               printf("%d\n",FD_ISSET(fd[1],fdsetw));// 0
               */
            if(FD_ISSET(fd[0],fdsetr)){
                printf("u could see , i could read\n");
                char line[1000]="";
                int n = read(fd[0],line,1000);
                //printf("hey%d\n",n);
                write(STDOUT_FILENO,line,strlen(line));
            }
            close(fd[0]);
            FD_ZERO(fdsetr);
            FD_ZERO(fdsetw);
            FD_ZERO(fdsete);
            fd[0]=open("tmp",O_RDONLY);
            FD_SET(fd[0],fdsetr);
        }
        close(fd[0]);
    }
}
void whole_block_select_basic_try2(){
    close(fd[0]);
    close(fd[1]);

    int a;
    while 
        (scanf("%d",&a)!=EOF){
            printf("%d\n",a);
            pid_t pid = fork();
            if(pid < 0)printf("fork error\n");
            else if (pid == 0){
                printf("hey , i am pson\n");
                FD_ZERO(fdsetr);
                FD_ZERO(fdsetw);
                FD_ZERO(fdsete);
                fd[1]=open("tmp",O_WRONLY);
                FD_SET(fd[1],fdsetw);
                int r=select(max(fd[0],fd[1])+1,fdsetr,fdsetw,fdsete,NULL);
                /*
                   printf("%d\n",r);// output 0
                   printf("%d\n",FD_ISSET(fd[0],fdsetr));// 0 
                   printf("%d\n",FD_ISSET(fd[1],fdsetw));// 0
                   */
                if(FD_ISSET(fd[1],fdsetw)){
                    char line[100]="";
                    sprintf(line,"i can write a = %d\n",a);
                    write(fd[1],line,strlen(line));
                }
                close(fd[1]);
            }
            else if(pid > 0){
                printf("hey , i am pfather\n");
                sleep(2);
                FD_ZERO(fdsetr);
                FD_ZERO(fdsetw);
                FD_ZERO(fdsete);
                fd[0]=open("tmp",O_RDONLY);
                FD_SET(fd[0],fdsetr);
                int r=select(max(fd[0],fd[1])+1,fdsetr,NULL,fdsete,NULL);
                /*
                   printf("%d\n",r);// output 0
                   printf("%d\n",FD_ISSET(fd[0],fdsetr));// 0 
                   printf("%d\n",FD_ISSET(fd[1],fdsetw));// 0
                   */
                if(FD_ISSET(fd[0],fdsetr)){
                    printf("u could see , i could read\n");
                    char line[1000]="";
                    int n = read(fd[0],line,1000);
                    //printf("hey%d\n",n);
                    write(STDOUT_FILENO,line,strlen(line));
                }
                close(fd[0]);
            }
        }
}

void select_basic(){
    FD_ZERO(fdsetr);
    FD_ZERO(fdsetw);
    FD_ZERO(fdsete);
    FD_SET(0,fdsetr);
    FD_SET(1,fdsetw);
    int r = select(2,fdsetr,fdsetw,NULL,NULL);
    printf("%d\n",r);
    if(FD_ISSET(0,fdsetr)){
        printf("0 is ready\n");
        char line[100]="";
        read(0,line,100);
        write(STDOUT_FILENO,line,40);
    }
    if(FD_ISSET(1,fdsetw)){
        printf("1 is ready\n");
        write(1,"hello select\n",100);
        //printf("\n__select_basic finish\n"); -- very strange....
    }
}
void select_basic_2(){
    FD_ZERO(fdsetr);
    FD_ZERO(fdsetw);
    FD_ZERO(fdsete);
    int fd = open("tmp",O_RDONLY);
    FD_SET(fd,fdsetr);
    int r = select(fd+1,fdsetr,fdsetw,NULL,NULL);
    printf("%d\n",r);
    if(FD_ISSET(fd,fdsetr)){
        printf("%d is ready\n",fd);
        char line[100]="";
        read(fd,line,100);
        write(STDOUT_FILENO,line,40);
    }
}
void select_basic_3(){
    FD_ZERO(fdsetr);
    FD_ZERO(fdsetw);
    FD_ZERO(fdsete);
    int fd = open("tmp",O_RDONLY);
    int fd2 = open("tmp",O_WRONLY);
    FD_SET(fd,fdsetr);
    FD_SET(fd2,fdsetw);
    int r = select((fd2>fd?fd2:fd)+1,fdsetr,fdsetw,NULL,NULL);
    printf("%d\n",r);
    if(FD_ISSET(fd,fdsetr)){
        printf("%d is ready to read\n",fd);
        char line[100]="";
        read(fd,line,100);
        write(STDOUT_FILENO,line,40);
    }
    if(FD_ISSET(fd2,fdsetw)){
        printf("%d is ready to write\n",fd2);
        write(fd2,"hello select for writing\n",100);
    }
}
void select_basic_4(){
    FD_ZERO(fdsetr);
    FD_ZERO(fdsetw);
    FD_ZERO(fdsete);
    int fd = open("tmp",O_RDONLY);
    int fd2 = open("tmp",O_WRONLY);
    FD_SET(fd,fdsetr);
    FD_SET(fd2,fdsetw);
    int r = select((fd2>fd?fd2:fd)+1,fdsetr,fdsetw,NULL,NULL);
    printf("%d\n",r);
    if(FD_ISSET(fd2,fdsetw)){
        printf("%d is ready to write\n",fd2);
        write(fd2,"hello select for writing\n",24);
    }
    if(FD_ISSET(fd,fdsetr)){
        printf("%d is ready to read\n",fd);
        char line[100]="";
        read(fd,line,100);
        write(STDOUT_FILENO,line,100);
    }
}

void select_sleep(){
    timeval * tvptr = (timeval*)malloc(sizeof(timeval));
    tvptr->tv_sec=1;
    tvptr->tv_usec=1000;
    int r = select(0,NULL,NULL,NULL,tvptr);
    printf("%d\n",r);
}


void pipe_select(){
    FD_ZERO(fdsetr);
    FD_ZERO(fdsetr);
    FD_ZERO(fdsetw);
    pid_t pid = fork();
    if(pid < 0){
        printf("fork error\n");
    }
    else if(pid == 0){
        close(fd[0]);
        int a;
        while(scanf("%d",&a)!=EOF){
            char *line = (char*)malloc(sizeof(char)*100);
            sprintf(line,"hello select %d\n",a);
            write(fd[1],line,20);
        }
    }
    else if(pid > 0){
        close(fd[1]);
        while(1){
            FD_ZERO(fdsetr);
            FD_SET(fd[0],fdsetr);
            int r = select(fd[0]+1,fdsetr,NULL,NULL,NULL);
            printf("%d\n",r);
            int cnt = 0;
            if(FD_ISSET(fd[0],fdsetr)){
                char line[100]="";
                int n = read(fd[0],line,100);
                write(STDOUT_FILENO,line,100);
                //write(STDOUT_FILENO,"good",100);// why this good come up two times?
            }
        }
    }
}
void sh_pipe_select(){
    FD_ZERO(fdsetr);
    FD_ZERO(fdsetr);
    FD_ZERO(fdsetw);
    pid_t pid = fork();
    if(pid < 0){
        printf("fork error\n");
    }
    else if(pid == 0){
        close(fd[0]);
        FD_ZERO(fdsetw);
        FD_SET(fd[1],fdsetw);
        int cnt = 0;
        while (cnt ++ < 10){
            int r = select(fd[1]+1,NULL,fdsetw,NULL,NULL);
            int a;
            char *line = (char*)malloc(sizeof(char)*100);
            sprintf(line,"hello select %d\n",cnt+20);
            if(FD_ISSET(fd[1],fdsetw)){
                write(fd[1],line,20);
                FD_ZERO(fdsetw);
                FD_SET(fd[1],fdsetw);
            }
            else{
                printf("hey , that is normal\n");
            }
        }
        close(fd[1]);
    }
    else if(pid > 0){
        close(fd[1]);
        while(1){
            char cmd[100] = " echo good \n sleep 2";
            if(system(cmd) == 0){
                FD_ZERO(fdsetr);
                FD_SET(fd[0],fdsetr);
                int r = select(fd[0]+1,fdsetr,NULL,NULL,NULL);
                printf("%d\n",r);
                int cnt = 0;
                if(FD_ISSET(fd[0],fdsetr)){
                    char line[100]="";
                    int n = read(fd[0],line,100);
                    write(STDOUT_FILENO,line,100);
                    //write(STDOUT_FILENO,"good",100);// why this good come up two times?
                }
            }
        }
    }
}
void sh_pipe_select_non_block(){
    FD_ZERO(fdsetr);
    FD_ZERO(fdsetr);
    FD_ZERO(fdsetw);
    pid_t pid = fork();
    if(pid < 0){
        printf("fork error\n");
    }
    else if(pid == 0){
        sleep(10);
        close(fd[0]);
        FD_ZERO(fdsetw);
        FD_SET(fd[1],fdsetw);
        int cnt = 0;
        while (cnt ++ < 10){
            timeval * tvptr = (timeval*)malloc(sizeof(timeval));
            tvptr->tv_sec = 0;
            tvptr->tv_usec = 0;
            int r = select(fd[1]+1,NULL,fdsetw,NULL,tvptr);
            int a;
            char *line = (char*)malloc(sizeof(char)*100);
            sprintf(line,"hello select %d\n",cnt+20);
            if(FD_ISSET(fd[1],fdsetw)){
                write(fd[1],line,20);
                FD_ZERO(fdsetw);
                FD_SET(fd[1],fdsetw);
            }
            else{
                printf("hey , that is normal\n");
            }
        }
        close(fd[1]);
    }
    else if(pid > 0){
        close(fd[1]);
        while(1){
            char cmd[100] = " echo good \n sleep 10 ";
            if(system(cmd) == 0){
                FD_ZERO(fdsetr);
                FD_SET(fd[0],fdsetr);
                timeval * tvptr = (timeval*)malloc(sizeof(timeval));
                tvptr->tv_sec = 0;
                tvptr->tv_usec = 0;
                int r = select(fd[0]+1,fdsetr,NULL,NULL,NULL);
                printf("%d\n",r);
                int cnt = 0;
                if(FD_ISSET(fd[0],fdsetr)){
                    char line[100]="";
                    int n = read(fd[0],line,100);
                    write(STDOUT_FILENO,line,100);
                    //write(STDOUT_FILENO,"good",100);// why this good come up two times?
                }
                else{
                    printf("read is not ready\n");
                }
            }
        }
    }
}

void basic_select(){
/* ./d_select_read_in.sh | unbuffer -p ./d_select | ./d_unbuffer_read_in.sh 4
	if((sn=select(STDOUT_FILENO+1,fdsetr,NULL,NULL,&tv))>0){
	the read and write process stay the same. a and b grows at the same time.
	}
	if((sn=select(STDOUT_FILENO+1,fdsetr,fdsetw,NULL,&tv))>0){
		could read , but if see from the terminal after a pipe to sleep , then , sees nothing.
	}
if the output flush is set as default.
./d_unbuffer_read_in.sh 0 < t | unbuffer -p ./d_select
	read and write at the same time , could read, but read is much more slower than write.
if the output flush buffer is closed,
*/
    FD_ZERO(fdsete);
    FD_ZERO(fdsetr);
    FD_SET(STDIN_FILENO,fdsetr);
    FD_ZERO(fdsetw);
    FD_SET(STDOUT_FILENO,fdsetw);
    timeval tv={1,1};
    int a = 0 , b = 0 , c= 0;
    char s[100] = "" ;
    while(1){
	FD_SET(STDIN_FILENO,fdsetr);
	FD_SET(STDOUT_FILENO,fdsetw);
	int sn=0;
	if((sn=select(STDOUT_FILENO+1,fdsetr,NULL,NULL,&tv))>0){
		if(FD_ISSET(STDIN_FILENO,fdsetr)){
			int m = 0;
			if(m = read(STDIN_FILENO,s,10000) == 0)break;
			a++;
		}
		else{
		}
		if(FD_ISSET(STDOUT_FILENO,fdsetw)){
			//printf("write ready!!:%s,%d,%d,%d,%d\n",s,sn,a,b,c); should not use printf , instead , should use write.
			char x[1000];
			sprintf(x,"writeready!!:%s,%d,%d,%d,%d\n",s,sn,a,b,c);
			write(STDOUT_FILENO,x,strlen(x));
			strcpy(s,"a");
			b++;
		}
	}
	c++;
    }
}
    int a = 0 , b = 0 , c= 0;
    char s[100] = "" ;
	int sn=0;
void basic_select_only_read(){
/* ./d_select_read_in.sh | unbuffer -p ./d_select | ./d_unbuffer_read_in.sh 4
	if((sn=select(STDOUT_FILENO+1,fdsetr,NULL,NULL,&tv))>0){
	the read and write process stay the same. a and b grows at the same time.
	}
	if((sn=select(STDOUT_FILENO+1,fdsetr,fdsetw,NULL,&tv))>0){
		could read , but if see from the terminal after a pipe to sleep , then , sees nothing.
	}
if the output flush is set as default.
./d_unbuffer_read_in.sh 0 < t | unbuffer -p ./d_select
	read and write at the same time , could read, but read is much more slower than write.
if the output flush buffer is closed,
*/
    FD_ZERO(fdsete);
    FD_ZERO(fdsetr);
    FD_SET(STDIN_FILENO,fdsetr);
    FD_ZERO(fdsetw);
    FD_SET(STDOUT_FILENO,fdsetw);
    timeval tv={1,1};
    int fd=open("a",O_WRONLY);
    while(1){
	FD_SET(STDIN_FILENO,fdsetr);
	FD_SET(STDOUT_FILENO,fdsetw);
	if((sn=select(STDOUT_FILENO+1,fdsetr,NULL,NULL,&tv))>0){
		if(FD_ISSET(STDIN_FILENO,fdsetr)){
			int m = 0;
			if(m = read(STDIN_FILENO,s,10000) == 0)break;
			char x[1000];
			sprintf(x,"writeready!!:%s,%d,%d,%d,%d\n",s,sn,a,b,c);
			write(STDOUT_FILENO,x,strlen(x));
			write(fd,x,strlen(x));
			strcpy(s,"a");
			a++;
		}
	}
	c++;
    }
}

void sigusr1(int signo){
	if(signo == SIGUSR1){
			char x[1000];
			sprintf(x,"writeready!!:%s,%d,%d,%d,%d\n",s,sn,a,b,c);
			write(STDOUT_FILENO,x,strlen(x));
			strcpy(s,"a");
	}
	else{
		printf("catch failure\n");
	}
}


int main(){
	if(signal(SIGUSR1,sigusr1)!=0){
		printf("sorry\n");
	}
	basic_select_only_read();
	//basic_select();
    if(pipe(fd)<0){
        printf("pipe error\n");
    }
    else{


        printf("init over\n");

        //non_block_select_basic();
        //non_block_select_waiting_basic();
        //select_basic();
        //select_basic_2();
        //select_basic_3();
        //select_basic_4();
        //select_sleep();
        //whole_block_select_basic_try2();
        /*
         * it is very important to init the fdset , with FD_ZERO.
         * */
        //whole_block_select_basic_try3();
        /*
         * whole block select basic try tries to fork a son process , and wait until read or write is ready for a fd of a file tm , we wanna that the write and read function could have block each other , but , in fact , as long as the existence of tmp , both are availble.
         * those functions just had told me what select could do.
         * */
        //pipe_select();
        //sh_pipe_select();
/*
	cant really get what above means.
*/
    }
    return 0;
}


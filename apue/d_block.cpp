#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <signal.h>

void set_fl(int fd,int flags){
    int val;
    if((val=fcntl(fd,F_GETFL,0))<0)
        printf("fcntl F_GETFL error\n");
    val |= flags;
    if(fcntl(fd,F_SETFL,val)<0)
        printf("set val error\n");
}

void block_basic(){
    int fd[2];
    if(pipe(fd)<0)
        printf("pipe error\n");
    pid_t pid = -1;
    pid = fork();
    if(pid < 0)
        printf("fork error\n");
    else if(pid == 0){
        close(fd[1]);
        int cnt = 0;
        while(cnt ++ < 5 ){
            char line[20] = "";
            int n = read(fd[0],line,20);
            char output[20] = "";
            sprintf(output,"n:%d;%s\n",n,line);
            n = write(STDOUT_FILENO,output,strlen(output));
        }
    }
    else if(pid > 0){
        close(fd[0]);
        int cnt = 0;
        while(cnt ++ < 10){
            char line[20] = "";
            sprintf(line,"hello world\n");
            int n = write(fd[1],line,strlen(line));
            sleep(2);
        }
    }
}

static void blocking(int signo){
    if(signo == 11){
        printf("hei , u know , that it is blocking now\n");
        exit(1);
    }
}

void non_read_block_basic(){
    if(signal(11,blocking)<0)
        printf("signal error\n");
    int fd[2];
    if(pipe(fd)<0)
        printf("pipe error\n");
    //set_fl(fd[0],O_NONBLOCK);
    set_fl(fd[1],O_NONBLOCK);
    pid_t pid = -1;
    pid = fork();
    if(pid < 0)
        printf("fork error\n");
    else if(pid == 0){
        close(fd[1]);
        int cnt = 0;
        while(cnt ++ < 10){
            char line[20] = "";
            int n = read(fd[0],line,20);
            char output[20] = "";
            sprintf(output,"%s\n",line);
            n = write(STDOUT_FILENO,output,strlen(output));
            sleep(1);
        }
    }
    else if(pid > 0){
        close(fd[0]);
        int cnt = 0;
        while(cnt ++ < 10){
            char line[20] = "";
            sprintf(line,"%d %d\n",cnt,cnt+1);
            int n = write(fd[1],line,strlen(line));
            sleep(2);
        }
    }
}
void non_write_block_basic(){
    if(signal(11,blocking)<0)
        printf("signal error\n");
    int fd[2];
    if(pipe(fd)<0)
        printf("pipe error\n");
    //set_fl(fd[0],O_NONBLOCK);
    set_fl(fd[1],O_NONBLOCK);
    pid_t pid = -1;
    pid = fork();
    if(pid < 0)
        printf("fork error\n");
    else if(pid == 0){
        close(fd[1]);
        int cnt = 0;
        while(cnt ++ < 10){
            char line[20] = "";
            int n = read(fd[0],line,20);
            char output[20] = "";
            sprintf(output,"%s\n",line);
            n = write(STDOUT_FILENO,output,strlen(output));
            sleep(3);
        }
    }
    else if(pid > 0){
        close(fd[0]);
        int cnt = 0;
        while(cnt ++ < 10){
            printf("nice\n");
            char line[20] = "";
            sprintf(line,"%d %d\n",cnt,cnt+1);
            int n = write(fd[1],line,strlen(line));
            // the write get blocked only when the pipe_buffer is full , and i have no idea how to set pipe_buff currently.
        }
    }
}

int main(){
    non_write_block_basic();
    //non_read_block_basic();
    //block_basic();
    return 0;
}

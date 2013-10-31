#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

void basic_test(){
    int pid=0;
    if((pid=fork())==0){
        execlp("/root/happyhan/demo/apue/get_argv.sh","0","22","33");
    }
    else{
        pid_t ppid=-1;
        int a;
        if((ppid=wait(&a))){
            printf("father,cpid:%d,%d,%d\n",pid,ppid,a);
        }
    }
}

int main(){
    return 0;
}

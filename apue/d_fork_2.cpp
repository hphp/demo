#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <errno.h>

void sig_child(int signo){
        if(signo == SIGCLD){
                int rc=waitpid(0,NULL,0);
                printf("returncode:%d\n",rc);
                if(signal(SIGCLD,sig_child)<=0){
                        printf("catch failure here.\n");
                }
        }
        else{
                printf("wrong number:%d vs %d\n",signo,SIGCLD);
        }
}


int main(){
        if(signal(SIGCLD,sig_child)<=0){
                printf("catch failure\n");
        }
        pid_t pid;
        if((pid = fork()) < 0){
                printf("fork failure\n");
        }
        else if(pid == 0){
                printf("this is the child.\n");
                if(execlp("/data/happyhan/demo/d_c/write.sh","write.sh","1",NULL) < 0){
                        printf("write.sh run failure,error no %d\n",errno);
                }
        }
        else{
                printf("subprocess id %d\n",pid);
                int a;
                while(scanf("%d",&a)!=EOF){
                        printf("%d\n",a);
                }
        }
        return 0;
}

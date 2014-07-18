#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <errno.h>

int main(){
        pid_t pid;
        if((pid = fork()) < 0){
                printf("fork failure\n");
        }
        else if(pid == 0){
                printf("this is the child.\n");
                if(execlp("/home/hphp/Documents/code/demo/demo/apue/root_test.sh","root_test.sh","1",NULL) < 0){
                        printf("root test.sh,%d\n",errno);
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

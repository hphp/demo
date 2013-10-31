#include <sys/wait.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

void basic_test(){
    pid_t pid=-1;
    FILE *f=NULL;
    if((pid=fork())==0){
    }
    else{
        int status=0;
        if(wait(&status)){
            f=popen("./get_argv.sh 1 2 3","r");
            printf("hi\n");
            char line[1000]="";
            int MAXLINE=100;
            if(f==NULL)return;
            while(fgets(line,MAXLINE,f)!=NULL){
                if(strlen(line)){
                    printf("%s",line);
                }
            }
        }
    }
}

int main(){
    basic_test();
    return 0;
}

#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <signal.h>
void basic_popen(){
    FILE * f = popen("md5sum a","r");
    char a[10000];
    fgets(a,200,f);
    char b[100],c[100];
    sscanf(a,"%s%s",c,b);
    printf("%s\n",c);
}

void pipe_basic(){
    int fd[2];
    int pid=-1;
    if(pipe(fd) < 0){
        printf("error\n");
    }
    else{
        if((pid=fork())<0){
            printf("fork error\n");
        }
        else{
            if(pid == 0){
                printf("hello i am son\n");
                sleep(2);
                close(fd[0]);
                write(fd[1],"hi,i am son\n",15);
            }
            else{
                printf("hello i am father\n");
                sleep(2);
                close(fd[1]);
                char line[1000];
                printf("ready for read\n");
                int n=read(fd[0],line,1000);
                write(STDOUT_FILENO,line,n);
            }
        }
    }
}

static void test(int signo){
    if(signo == SIGPIPE)
        printf("here u are signo:%d\n",signo);
}

void pipe_basic_close(){
    int fd[2];
    int pid=-1;
    if(signal(SIGPIPE,test)==SIG_ERR)
        printf("signal error\n");
    if(pipe(fd) < 0){
        printf("error\n");
    }
    else{
        if((pid=fork())<0){
            printf("fork error\n");
        }
        else{
            if(pid == 0){
                sleep(2);
                printf("hello i am son\n");
                close(fd[0]);
                int n = write(fd[1],"hi,i am son\n",15);
                printf("n:%d\n",n);
                /*
                if(n < 0)
                    test(SIGPIPE);
                    */
            }
            else{
                close(fd[1]);
                close(fd[0]);;
                return;
                printf("hello i am father\n");
                sleep(2);
                close(fd[1]);
                char line[1000];
                printf("ready for read\n");
                int n=read(fd[0],line,1000);
                write(STDOUT_FILENO,line,n);
            }
        }
    }
}
void pipe_loop_close(){
    int fd[2];
    int pid=-1;
    if(signal(SIGPIPE,test)==SIG_ERR)
        printf("signal error\n");
    if(pipe(fd) < 0){
        printf("error\n");
    }
    else{
        if((pid=fork())<0){
            printf("fork error\n");
        }
        else{
            if(pid == 0){
                close(fd[0]);
                int cnt = 0 ;
                while(cnt++ < 10){
                    int n = write(fd[1],"hi,i am son\n",15);
                    printf("n:%d\n",n);
                    sleep(3);
                }
            }
            else{
                close(fd[1]);
                int cnt = 0;
                while(cnt ++ < 20){
                    char line[1000];
                    int n=read(fd[0],line,1000);
                    write(STDOUT_FILENO,line,n);
                    if(cnt == 5)
                        close(fd[0]);
                }
            }
        }
    }
}

int main(){
    pipe_loop_close();
    //pipe_basic_close();
    //pipe_basic();
    //basic_popen();
    return 0;
}

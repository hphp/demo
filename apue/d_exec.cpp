#include <stdio.h>
#include <unistd.h>

void basic_test(){
    int pid=0;
    if((pid=fork())==0){
        execlp("/root/happyhan/demo/apue/d_pipe","1","2","3");
    }
    else{
        printf("father,cpid:%d\n",pid) ;
    }
}
void path_test(){
    int pid=0;
    if((pid=fork())==0){
        // if there is no in the first argv , there wont get anything to be done.
        execlp("","/root/happyhan/demo/apue/get_argv.sh","2","3");
        execlp("get_argv.sh","get_argv.sh","2","3");
    }
    else{
        printf("father,cpid:%d\n",pid) ;
    }
}
void argv_test(){
    int pid=0;
    if((pid=fork())==0){
        execlp("/root/happyhan/demo/apue/get_argv.sh","0","2","3");
    }
    else{
        printf("father,cpid:%d\n",pid) ;
    }
}

int main(){
    //argv_test();
    path_test();
    return 0;
}

#include <stdio.h>
#include <unistd.h>
/*
 * this function is test for a parent process creating several child processes
 * */
int main(){
    int i = 0 , stat = 0;
    for(i = 0 ;i < 2 ; i ++){
        stat = fork();
        if(stat == 0 || stat == -1)break;
    }
    if(stat == 0){
        if(i == 0){
            printf("%dxx - this process id is %d , and it is scheduler\n",i,getpid());
        } 
        else if(i == 1){
            printf("%d yy - this process id is %d ,and it is worker\n",i,getpid());
        }
    }
    else{// father
        printf("%d xx this process id is %d , and it is father\n",i,getpid());
    }
    return 0;
}

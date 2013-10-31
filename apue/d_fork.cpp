#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

void pson_input(){
    pid_t pid = -1;
    pid=fork();
    int a;
    if(pid < 0){
        printf("fork error\n");
    }
    else if(pid == 0){
        while(scanf("%d",&a)!=EOF){
            printf("%d\n",a);
        }
    }
    else if(pid > 0){
        printf("hey father\n");
    }
}

int cnt = 0;
void same_pro(){
    /*
     *
     * i wanna this program to calculate sth in the main process , and do sth else using son p , but , the data between them can share right now.
     * */
    pid_t pid = -1;
    pid=fork();
    if(pid < 0)
        printf("fork error\n");
    else if(pid == 0){
        cnt ++; 
    }
    else if(pid > 0){
        char cmd[100] = "echo u are right \n sleep 3";
        if(system(cmd) == 0){
            printf("%d\n",cnt);
        }
    }
}

int main(){
    //pson_input();
    same_pro();
    return 0;
}

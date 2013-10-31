#include <stdio.h>
#include <fcntl.h>
#include <string.h>
#include <unistd.h>
#include <sys/stat.h>
#include <sys/types.h>
int main(){
    char s[100]="abcdefg";
    while(scanf("%s",s)!=EOF){
        /*
        int fd = open("d_open.out",O_WRONLY);
        if(fd < 0){
            printf("open fail\n");
            creat("d_open.out",O_RDWR);
            fd = open("d_open.out",O_WRONLY);
            if(fd < 0){
                printf("open fail again\n");
                continue;
            }
        }
        if(lseek(fd,0L,2)<0){
            printf("lseek fail\n");
        }
        */
        int fd = open("d_open.out",O_APPEND|O_RDWR);
        if(fd < 0){
            printf("open fail\n");
        }
        else{
            printf("fd:%d %m\n",fd);
            int wr=write(fd,s,strlen(s));
            if(wr!=strlen(s)){
                printf("nonsense:%d %m\n",wr);
            }
        }
        close(fd);
    }
    return 0;
}

#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>

/*
 * when set to seek_end , then , the fgets will get from the current pos
 * */

int main(){
    FILE * f = fopen("d_fseek.in","a+");
    int fs = fseeko(f,0,SEEK_END);
    printf("fs%d\n", fs );

    char a[100] = "2222";
    while(1){
        if(fgets(a,10,f)!=NULL){
            printf("__%s__",a);
        }
        sleep(2);
    }

    fwrite(a,sizeof(char),strlen(a), f);
    fclose(f);
    return 0;
}

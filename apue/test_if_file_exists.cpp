#include <stdio.h>
#include <sys/stat.h>

int main(){
    char temp[10]="a";
    struct stat st;
    int s=stat(temp,&st);
    printf("%d\n",s);
    return 0;
}

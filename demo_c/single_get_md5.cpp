#include <stdlib.h>
#include <stdio.h>
#include <sys/stat.h>

#define MAX_FILE_DEEP 255
#define MAX_FILE_NAME_LEN 255*MAX_FILE_DEEP

char * get_md5_of_file(char *file){
    struct stat st;
    if(stat(file,&st) != 0){
        return "-1";
    }

    char request[MAX_FILE_NAME_LEN]="";
    sprintf(request,"md5sum %s",file);
    FILE *f = popen(request,"r");
    char whole[100]="";
    fgets(whole,100,f);
    char a[10],md5[100]="";
    sscanf(whole,"%s%s",md5,a);
    printf("%s\n",md5);
    return md5;
}

int main(){

    char filename[10000] = "a";
    char *s  = get_md5_of_file(filename);
    printf("%s\n",s);
    return 0;
}

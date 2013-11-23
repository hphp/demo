#include <stdio.h>
#include <fcntl.h>
#include <string.h>
#include <unistd.h>

int main(){

    int fd = open("d_fdopen.in",O_RDONLY|O_WRONLY|O_CREAT);
    off_t t = lseek(fd,0,SEEK_END);
    printf("offset %d %d\n",fd,t);
    FILE * f = fdopen(fd,"w");
    char a[100] = "22222222222222222222222";
    int fn = fwrite(a,sizeof(a),strlen(a),f);
    printf("write number %d\n",fn);
    close(fd);
    fclose(f);
    return 0;

}

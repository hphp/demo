#include <sys/stat.h>
#include <stdio.h>

void basic_test(){
    char path[1000]="/root/happyhan/dl_support/http.20120905_38";
    //char path[1000]="~/happyhan/dl_support/http.20120905_38";
    //there maybe no ascii char as ~
    // output bytes: the exact same length with ll result.
    struct stat st;
    int r=stat(path,&st);
    if(r==0){
        printf("good%d\n",st.st_size);
    }
    else{
        printf("%d\n",r);
    }
}
int main(){
    //basic_test();
    return 0;
}

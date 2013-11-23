#include <stdio.h>
#include <sys/time.h>
long gettime_usec(){
    timeval tv;
    gettimeofday(&tv,NULL);
    return tv.tv_usec;
}

int main(){
    printf("%ld\n",gettime_usec());
};

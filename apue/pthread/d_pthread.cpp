#include <pthread.h>
#include <stdio.h>
#include <unistd.h>
void print(){
    printf("good\n");
    /*
    int a;
    while(scanf("%d",&a)!=EOF){
        printf("good\n");
    }
    */
}

void * thr_fn(void * args){
    print();
    printf("cood\n");
    return ((void*) 0);
}

int main(){
    pthread_t tidp;
    pthread_attr_t attr;
    int a = pthread_create(&tidp,NULL,thr_fn,NULL);
    sleep(6);
    printf("hey,%d\n",a);
    print();
    return 0;
}

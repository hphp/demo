#include <pthread.h>
#include <stdio.h>
#include <unistd.h>

pthread_mutex_t pmt = PTHREAD_MUTEX_INITIALIZER;

void print(int * x){
    pthread_mutex_lock(&pmt);
    int c = 0;
    while(c < 2){
        printf("good %d\n",*(x));
        sleep(1);
        c++;
    }
    pthread_mutex_unlock(&pmt);
    /*
    int a;
    while(scanf("%d",&a)!=EOF){
        printf("good\n");
    }
    */
}


void * thr_fn(void * args){
    print((int *)args);
    printf("cood\n");
    return ((void*) 0);
}

int main(){
    pthread_t tidp;
    pthread_t tidpb;
    int c = 0;
    int a = pthread_create(&tidp,NULL,thr_fn,(void*)(&c));
    int d = 1;
    int b = pthread_create(&tidpb,NULL,thr_fn,(void*)(&d));
    sleep(6);
    printf("hey,%d\n",a);
    int e = 2;
    print(&e);
    return 0;
}

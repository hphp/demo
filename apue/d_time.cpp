#include <time.h>
#include <stdio.h>

int main(){
    time_t rawtime;
    struct tm* timeinfo;

    time( & rawtime );
    timeinfo = localtime( &rawtime );
    printf("%d\n",timeinfo->tm_year+1900);
    printf("%d\n",timeinfo->tm_mon+1);
    printf("%d\n",timeinfo->tm_mday);
    printf("%d\n",timeinfo->tm_sec);
    printf("%d\n",timeinfo->tm_hour);
    printf("%d\n",timeinfo->tm_min);
    return 0;
}

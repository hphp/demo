#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main(){
    char *a = (char*)malloc(sizeof(char)*100);
    strcpy(a,"abcd efg|xxxxxx  xxx |xxc");
    char *s = a;
    while((*s)!='\0'){
        char *b = (char*)malloc(sizeof(char)*100);
        sscanf(s,"%[^|]|",b);
        printf("__%s__\n",b);
        s += strlen(b);
        while((*(s++))==' ');
        free(b);
    }
    return 0;
}

#include <stdio.h>
#include <string.h>

int main(){
	char a[10000];
	char * ptr;
	while(scanf("%s",a)!=EOF){
		printf("%d",a);
		ptr = strtok(a,"|");
		printf("%d",ptr);
		while(ptr!=NULL){
			printf(",%s,\n",ptr);
			printf("%d",ptr);
			ptr=strtok(NULL,"|");
		}
	}
	return 0;
}

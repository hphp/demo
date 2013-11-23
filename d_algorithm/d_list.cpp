#include <stdio.h>
#include <stdlib.h>
#include <string>
using namespace std;

struct bList{
	int b;
	char c[100];
	bList * last;
	bList * next;
};
/*
when bList{
	string a;
}
bList * list = (bList*)malloc(sizeof(bList));
list->a -- segment fault.
*/

int main(){
	bList * list = (bList*)malloc(sizeof(bList));
	string a = "x";
	list->b = 2;
	printf("good\n");
	strcpy((*list).c,"xx");
	printf("%s\n",((*list).c));
	return 0;
}

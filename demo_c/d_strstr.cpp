#include <stdio.h>
#include <string.h>

int main(){
	char s[100] = "dlql.qq.com";
	char * a = strstr(s,"ql.qq.com");
	printf("%s,%d\n",a,strcmp("ql.qq.com",a));
	return 0;
}

#include <stdio.h>
#include <sys/stat.h>
#include <errno.h>
#include <string.h>

void basic_test(){
	int r = mkdir("/data/xx",0777);
	printf("%d,%d\n",r,errno);
}
void multi_layer_dir(){
	int r = mkdir("/data/xx/xx/xx/xx",0777);
	printf("%d,%d\n",r,errno);
}

void if_exist(){
	int r = mkdir("/data/happyhan/a",0777);
	printf("%d\n",r);
}

void makedir(char * pathname){
	int len = strlen(pathname);
	for(int i = 0; i < len; i ++){
		if(pathname[i] == '/'){
			pathname[i] = '\0';
			if(mkdir(pathname,0777)<0){
				printf("exist");
			}
			else{
				printf("mkdir ok %s\n",pathname);
			}
			pathname[i] = '/';
		}
	}
}

void makedir_test(){

	char pathname[100];
	scanf("%s",pathname);
	makedir(pathname);
	printf("ori:%s\n",pathname);
}
int main(){
	//multi_layer_dir();// cant mk more than one layer of directory;
	makedir_test();
	//if_exist();
	return 0;
}

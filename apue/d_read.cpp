#include <stdio.h> 
#include <unistd.h>
#include <stdlib.h>

void basic_rm_file_test(){

	while(true){
	FILE * f = fopen("d_read.in","r");
	if ( f != NULL){
		char line[1000];
		int input_max_length=1000;
		while(fgets(line,input_max_length,f)!=NULL){
			printf("%s",line);
			sleep(1);
		}
		system("echo > d_read.in");
		printf("rm d_read.in\n");
		fclose(f);
	}
}
}

void read_in_pipe(){
	char cmd[1000];
	sprintf(cmd,"./generate_continous_number.sh");
	FILE *f = popen(cmd,"r");
	if(f == NULL)
		printf("cant open\n");
	else{
		int read_in_number=0;
		char line[1000];
		int input_max_length=1000;
		while(fgets(line,input_max_length,f)!=NULL){
			read_in_number++;
			printf("%s",line);
			if(read_in_number > 10){
				printf("hei , here , we output larger than 10\n");
				sleep(2);
				read_in_number = 0;
				continue;
		}
		sleep(1);
	}
}
}

int main(){
	//basic_rm_file_test();
	read_in_pipe();
	return 0;
}

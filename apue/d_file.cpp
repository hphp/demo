#include <stdio.h>
#include <string>

using namespace std;

int main(){
    string log_name = "/root/happyhan/dl_support/http.20120905_38";
    //string log_name = "../http.20120914_38";
    FILE * fp = fopen(log_name.c_str(),"r");
    char ch; 
    int line_number=0;
    while((ch=fgetc(fp))!=EOF){
        if(ch == '\n')line_number++;
    }  
    printf("%d\n",line_number);
    return 0;
}

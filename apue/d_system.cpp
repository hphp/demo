#include <stdlib.h>
#include <stdio.h>
#include <iostream>
using namespace std;

void basic_system(){

    int return_code = system("echo good");
    printf("%d\n",return_code);
}

void output_str(){
    system("md5sum a");
}
void get_md5(){
    // this function doesnt work
    system("md5sum a | 1");
    char s[100];
    scanf("%s",s);
    cout << "s:" << s << endl;
}

int main(){
    //output_str();
    return 0;
}

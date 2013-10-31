#include <string>
using namespace std;

string hp_replace(string a,string from,string to){
    int i = 0 ;
    string b = a;
    i = b.find(from);
    while(i >= 0 && i < b.length()){
        a = b.replace(i,from.length(),to);
        b = a;
        i = b.find(from,i+2);
    }
    return b;
}

void test_hp_replace(){

    char a[10000]="";
    scanf("%s",a);
    string new_s = hp_replace(a,"(","\\(");
    printf("%s\n",new_s.c_str());
}

int main(){
    test_hp_replace();
    return 0;
}

#include <algorithm>
#include <string>
#include <set>
using namespace std;

void basic_test(){
    set<int> s;
    int cnt =0;
    int a;
    while(scanf("%d",&a)){
        set<int>::iterator i = s.find(a);
        if(i==s.end()){
            s.insert(a);
        }
        else{
            printf("already exists\n");
        }
    }
}


// kind of important to define it.
/*
struct A{
    int a,b; 
};
bool operator<(const A& a,const A& b){
    if(a.a==b.a)
        return a.b > b.b;
    return a.a > b.a;
}
*/
struct A{
    string a;
    string b;
    int c;
};
bool operator<(const A& a,const A& b){
    if(a.c==b.c){
        if(a.a==b.a) 
            return a.b<b.b;
        return a.a < b.a;
    }
    return a.c > b.c;
}
void structure_test(){
    set<A> s;
    char a[100000],b[1000000];
    int c;
    while(scanf("%s%s%d",a,b,&c)){
        A ac={a,b};
        //A ac={a,b,c};
        set<A>::iterator i = s.begin();
        printf("%s\n%s\n%d\n",(*i).a.c_str(),(*i).b.c_str(),i->c);
        i = s.find(ac);
        if(i==s.end()){
            ac.c=c;
            s.insert(ac);
        }
        else{
            printf("already exists,here update\n");
            ac.c=(i->c)+c;
            s.erase(i);
            s.insert(ac);
        }
    }

}

int main(){
    structure_test();
    return 0;
}

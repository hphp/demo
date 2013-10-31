#include <stdio.h>
#include <map>
#include <string>
using namespace std;

struct Info{
    int a;
    int b;
};

map<string,Info> mapx;

int main(){
    Info info = {1,2};
    Info info_2 = {4,3};
    /*
    mapx["a"]=info;
    mapx["b"]=info_2;
    */
    string xx = "a";
    map<string,Info>::iterator it;
    it=mapx.begin();
    mapx.insert(it,pair<string,Info>(xx,info));
    it = mapx.find(xx);

    if(it != mapx.end()){
        Info info = it->second;
        printf("%d\n",info.b);
    }
    return 0;
}

#include <stdio.h>
#include <map>
#include <string>
#include <set>
#include <sys/stat.h>
#include <unistd.h>
#include <time.h>
#include <signal.h>
#include <stdlib.h>
#include <fcntl.h>
#include <string.h>
using namespace std;

#define HAVEDONE 3
#define BEING_LOADING 2
#define BEING_WAITING 1
#define ORI_STATUS 0 
#define STOP_LIMITS 10
#define WAITING_LIMIT 10
#define LOAD_LIMIT 10
#define MAX 10000000000LL
#define DATA_LOG_MAX_LEN 1000000
#define INPUT_MAX_LEN 1000000
#define ONE_DAY_SEC 86400 
struct Info{
    string filename;
    long long std_len;
    long long cur_len;
    int status;// 0 for to be load , 1 for already output to load , 2 for loading , 3 for loaded.
    int request_num;
    int stop_time;
    string cur_filename;
    int wait_turn;
    int load_done_time;
    int last_request;
	int first_request;
};
map<string,Info> file_info;
struct Record{
    string url;
    string filename;
    int rnum;
};
struct comp{
    inline bool operator()(const Record& a,const Record& b){ 
        if(a.rnum ==b.rnum ){
            if(a.url==b.url) 
                return a.filename<b.filename;
            return a.url < b.url;
        }   
        return a.rnum > b.rnum;
    }
};
set<Record,comp> record_list;
char a[10000],b[100000];
int c;
set<Record,comp>::iterator it;

int main(){

	printf("record_list size:%d\n",record_list.size());
	int d;
	while(scanf("%s%s%d",a,b,&d)!=EOF){
		Record m={a,b,d};
		it=record_list.find(m);
		int rnum=0;
		if(it == record_list.end()){
			printf("cant find %s,%s\n",a,b);
		}
		else{
			rnum=it->rnum;
			printf("could find , %s,%s,%d\n",it->url.c_str(),it->filename.c_str(),it->rnum);
			record_list.erase(m);
		}
		m.rnum=(rnum)+d;
		record_list.insert(m);
		printf("%d\n",record_list.size());
		for(it = record_list.begin();it!=record_list.end();it++){
			printf("%s,%s,%d\n",it->url.c_str(),it->filename.c_str(),it->rnum);
		}
	}
	return 0;

}

#include <stdio.h>
#include <string.h>
#include <string>
using namespace std;

string ope[2000];
int s=0;
int e=0;
int is_ope(char a){
    if(a=='+')return 1;
    if(a=='-')return 1;
    if(a=='*')return 1;
    if(a=='/')return 1;
    return 0;
}
int is_ope_s(string s){
    if(s.length() != 1)return 0;
    char a = s[0];
    if(a=='+')return 1;
    if(a=='-')return 1;
    if(a=='*')return 1;
    if(a=='/')return 1;
    return 0;
}

int pair_h(int ss){
    int cnt = 0;
    for(int i = ss ; i < e ; i ++){
        if(ope[i] == "(")
            cnt++;
        else if(ope[i] == ")")
            cnt--;
        if(cnt == 0)
            return i;
    }
    return -1;
}
int pair_h_r(int ee){
    int cnt = 0;
    for(int i = ee ; i >= s ; i --){
        if(ope[i] == "(")
            cnt++;
        else if(ope[i] == ")")
            cnt--;
        if(cnt == 0)
            return i;
    }
    return -1;
}

int invalid(int ss){
    if(ss < s || ss >= e)
        return 1;
    return 0;
}

int cal(int ss,int ee , int * results){
    if(invalid(ss))return -1;
    if(invalid(ee))return -1;
    if( ss > ee )return -1;
    if( ss == ee ){
        int c =0;
        for(int i=0;i<ope[ss].length() ; i ++){
            if((ope[ss][i]>='0'&&ope[ss][i]<='9')){
            }
            else if (ope[ss][i] == '-'){
                if(c == 1)return -1;
                c++;
            }
            else if (ope[ss][i] == '+'){
                if(c == 1)return -1;
                c++;
            }
            else return -1;
        }
        int a;
        sscanf(ope[ee].c_str(),"%d",&a);
        (*results)=a;
        return 1;
    }
    else{
        string start = ope[ss];
        string end = ope[ee];
        //printf("ss:%dee:%d,%s,%s\n",ss,ee,ope[ss].c_str(),ope[ee].c_str());
        while((ope[ss]=="(")&&(ope[ee]==")")&&(ss<=ee)){ss++;ee--;}
        //printf("ss:%dee:%d,%s,%s\n",ss,ee,ope[ss].c_str(),ope[ee].c_str());
        if(invalid(ss))return -1;
        if(invalid(ee))return -1;
        if(ss > ee )return -1;
        if(is_ope_s(ope[ss])!=1){
            if(ss!=ee)
                return -1;
            else{
                return cal(ss,ee,results);
            }
        }
        else{
        
            int curss = ss+1;
            int pair_ha= pair_h(curss);
            if(pair_ha > ee)return -1;
            int a = -1;
            int ra = cal(curss,pair_ha,&a);
            if(ra < 0)return ra;
            (*results)=a;
            curss = pair_ha + 1;
            //printf("%dee%d\n",ss,ee);
            while ( curss <= ee ){
                int b = -1;
                int pair_hb = pair_h(curss);
                if(pair_hb > ee)return -1;
                //printf("::%d %d\n",curss,pair_hb);
                int rb = cal(curss,pair_hb,&b);
                if(rb < 0)return rb;
                a = *results;
                //printf("here%d\n",a);

                if(ope[ss][0] == '+')
                    (*results) = (int)(a + b);
                if(ope[ss][0] == '-')
                    (*results) = (int)(a - b);
                if(ope[ss][0] == '*')
                    (*results) = (int)(a * b);
                if(ope[ss][0] == '/'){
                    if(b == 0)return -1;
                    (*results) = (int)(a / b);
                }
                curss = pair_hb + 1;
            }
        }
        return 1;
    }
}


int avl(char s[]){
    int flag = 0;
    for(int i=0;i<strlen(s);i++)
        if(s[i]=='('){
            flag+=1;
            break;
        }
    for(int i=0;i<strlen(s);i++)
        if(s[i]==')'){
            flag+=10;
            break;
        }
    if(flag == 0)
        return 0;
    else if(flag == 1){
        int i =0;
        while( i < strlen(s)){
            if(s[i]!='(')break;
            i++;
        }
        while( i < strlen(s)){
            if(is_ope(s[i]) < 0)
                return -1;
            i++;
        }
        return 1;
    }
    else if(flag == 10){
        int i =0;
        while( i < strlen(s)){
            if(s[i]==')')break;
            if((s[i]<'0'||s[i]>'9')&&(s[i]!='-'))return -1;
            i++;
        }
        while( i < strlen(s)){
            if(s[i] != ')')
                return -1;
            i++;
        }
        return 2;
    }
    else{
        int i =0;
        while( i < strlen(s)){
            if(s[i]!='(')break;
            i++;
        }
        int j = strlen(s)-1;
        while( j >= i ){
            if(s[j]!=')')break;
            j--;
        }
        while(i<=j){
            if(s[i]<'0'||s[i]>'9')return -1;
            i++;
        }
        return 3;
    }
}

int main(){
    char *line = (char*)malloc(sizeof(char)*10000);
    while(gets(line)!=NULL){
        printf("%s\n",line);
        int cnt = 0;
        int len = strlen(line);
        s = 0;
        e = 0;
        int ans = 0;
        while((*line) != '\0'){
            char s[4]="";
            sscanf(line,"%s",s);
            int t = avl(s);
            //printf("t:%d\n",t);
            char tt[30] = "";
            if(t == -1)
            {
                ans = -1;break;
            }
            else if(t == 0){
                ope[e] = s;
                e ++;
            }
            else if(t == 1){
                int ct=0;
                for(int i = 0 ;i < strlen(s);i ++){
                    if(s[i] == '('){
                        tt[0]='(';
                        tt[1]='\0';
                        ope[e] = tt;
                        e++;
                    }
                    else{
                        tt[ct]=s[i];
                        ct++;
                    }
                }
                if(ct>0){
                    tt[ct]='\0';
                    ope[e]=tt;
                    e++;
                }
            }
            else if(t == 2){
                int ct=0;
                int i =0 ;
                while(s[i]!=')'){
                    tt[ct]=s[i];
                    ct++;
                    i++;
                }
                if(ct>0){
                    tt[ct]='\0';
                    ope[e]=tt;
                    e++;
                }

                while(i<strlen(s)){
                    tt[0]=s[i];
                    tt[1]='\0';
                    ope[e] = tt;
                    e++;
                    i++;
                }
            }
            else if(t == 3){
                int ct=0;
                int i =0 ;
                while(s[i] == '('){
                    tt[0]=s[i];
                    tt[1]='\0';
                    ope[e] = tt;
                    e++;
                    i++;
                }
                while(s[i]!=')'){
                    tt[ct]=s[i];
                    ct++;
                    i++;
                }
                if(ct>0){
                    tt[ct]='\0';
                    ope[e]=tt;
                    e++;
                }

                while(i<strlen(s)){
                    tt[0]=s[i];
                    tt[1]='\0';
                    ope[e] = tt;
                    e++;
                    i++;
                }
            }
            while((*line)==' ')line++;
            line += strlen(s);
            while((*line)==' ')line++;
            if(cnt++ >= len)break;
        }
        for(int i = 0 ;i < e ; i ++)
            printf("%s\n",ope[i].c_str());
        if(ans < 0){
            printf("Syntax Error\n");
            continue;
        }
        int results=0;
        ans = cal(s,e-1,&results);
        if(ans < 0){
            printf("Syntax Error\n");
        }
        else
            printf("%d\n",results);
    }
    return 0;
}

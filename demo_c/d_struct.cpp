
struct Info{
    int a,b;
};
void basic_struct(){
    Info info = {1,2};
}

void struct_list(){
    Info info[10];
    //info[1] = {1,2};// can not , because have already initialized.
    info[1].a = 1; info[1].b = 2;
}

int main(){
    //basic_struct();
    struct_list();
}

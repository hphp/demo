#include <sys/msg.h>
#include <errno.h>
#include <stdio.h>

int main(){
    printf("%d\n",EACCES);
    printf("%d\n",EEXIST);
    printf("%d\n",ENOENT);
    printf("%d\n",ENOSPC);

    // below is msgctl
    printf("%d\n",EINVAL);
    printf("%d\n",EPERM);
    printf("%d\n",EPERM);
    printf("%d\n",EACCES);
    return 0;
}

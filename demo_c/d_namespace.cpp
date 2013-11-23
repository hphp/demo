#include <stdio.h>
#include "d_namespace_include.h"
namespace abcpriv{
    void good(){
        printf("good\n");
    }
}

namespace abc{
    void good(){
        abcpriv::good();
     }
};

void basic_test(){
    abc::good();
    abcpriv::good();
}

int main(){
    //basic_test();
    dni::xx();
    return 0;
}

#include <stdio.h>


int euklid_ggT(int a, int b){

    int r = 0;

    do {
        //printf("%d | %d | %d\n", a, b, r);
        r = a % b;
        //printf("%d | %d | %d\n", a, b, r);
        a = b;
        b = r;
    } while (r != 0);

    return a;

}


int euklid_ggT_rec(int a, int b){

    int r = a % b;
    a = b;
    b = r;

    if(r == 0){
        return a;
    }
        
    return euklid_ggT_rec(a, b);

}


int main(){

    int n = 32;
    int m = 40;
    int res;


    //res = euklid_ggT(n, m);
    res = euklid_ggT_rec(n, m);

    printf("Result: %d\n", res);

}
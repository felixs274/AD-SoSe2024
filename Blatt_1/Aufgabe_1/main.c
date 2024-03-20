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



int main(){

    int n = 32;
    int m = 40;
    int res;


    res = euklid_ggT(n, m);
    

    printf("Result: %d\n", res);

}
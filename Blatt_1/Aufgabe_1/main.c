/* 
In Zusammenarbeit mit Daniel Heisig
*/ 

#include <stdio.h>


int ggT(int a, int b){

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


int ggT_rec(int a, int b){

    int r = a % b;
    a = b;
    b = r;

    if(r == 0){
        return a;
    }
        
    return ggT_rec(a, b);

}


int kgV(int a, int b){

    int i = 1;

    while( !((i%a==0) && (i%b==0)) ){
        i++;
    }

    return i;

}


int main(){

    int n = 32;
    int m = 40;
    int res;


    //res = ggT(n, m);
    //res = ggT_rec(n, m);
    //res = kgV(n, m);


    printf("kgV(%d, %d):   %d\n", n, m, kgV(n, m));
    printf("ggT(%d, %d):   %d\n", n, m, ggT(n, m));
    printf("%d x %d:       %d\n", n, m, (n*m));


    //printf("Result: %d\n", res);

}
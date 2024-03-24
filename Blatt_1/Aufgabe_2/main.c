/* 
In Zusammenarbeit mit Daniel Heisig
*/ 

#include <stdio.h>
#include <stdlib.h>


void init_list(int *l,  int n){

    for (int i = 2; i <= n; i++){
        l[i]=i;
    }

}


void print_list(int *l,  int n){

    printf("\n");
    for (int i = 2; i <= n; i++){
        printf("%d, ", l[i]);
    }
    printf("\n");

}


void print_list_primes(int *l,  int n){

    printf("\n");
    for (int i = 2; i <= n; i++){
        if (l[i] != 0){
            printf("%d, ", l[i]);
        }
    }
    printf("\n");

}


void sieb(int *l,  int n){

    for (int i = 2; i <= n; i++){

        if (l[i] != 0){

            for (int j = i+1; j <= n; j++){

                if (l[j]%l[i]==0){
                    l[j] = 0;
                } 
            }    
        }   
    }
}


int main(){

    int n = 100000;

    int list[n]; 

    init_list(list, n);
    //print_list(list, n);
    sieb(list, n);
    print_list_primes(list, n);
    
    
    return 0;

}
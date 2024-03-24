/* 
In Zusammenarbeit mit Daniel Heisig
*/ 

#include <stdio.h>
#include <stdlib.h>
#include <time.h>


#define MAX_RAND_INT 5


typedef struct {
    int rows;
    int cols;
    int *data;
} matrix;


matrix *Init(int rows, int cols){

    //Allocate memory for matrix struct
    matrix *m = (matrix *)malloc(sizeof(matrix));
    //Insert rows and colums into the matrix struct
    m->rows = rows;
    m->cols = cols;
    //Allocate memory for the Array
    m->data = (int *)calloc(rows, sizeof(int)*cols);

    return m;

}


void Print(matrix *m) {

    for (int i = 0; i < m->rows; i++) {
        for (int j = 0; j < m->cols; j++) {
            printf("%d ", m->data[i * m->cols + j]);
        }
        printf("\n");
    }
    
    printf("\n");

}


void Input(matrix *m) {

    printf("Enter values (%d x %d):\n", m->rows, m->cols);

    for (int i = 0; i < m->rows; i++) {
        for (int j = 0; j < m->cols; j++) {
            printf("(%d, %d): ", i + 1, j + 1);
            scanf("%d", &(m->data[i * m->cols + j]));
        }
    }
    printf("\n");
}


void RandomFill(matrix *m) {
    for (int i = 0; i < m->rows; i++) {
        for (int j = 0; j < m->cols; j++) {
            m->data[i * m->cols + j] = rand()%MAX_RAND_INT;
        }
    }
}


matrix *Add(matrix *a, matrix *b){

    if((a->rows != b->rows) || (a->cols != b->cols)){
        printf("Matrices are not the same size!\n");
        exit(EXIT_FAILURE);
    }

    matrix *c = Init(a->rows, a->cols);

    for (int i = 0; i < a->rows; i++) {
        for (int j = 0; j < a->cols; j++) {
            c->data[i * c->cols + j] = (a->data[i * a->cols + j]) + (b->data[i * b->cols + j]);
        }
    }

    return c;

}


matrix *Mult(matrix *a, matrix *b){

    if((a->rows != b->cols) || (a->cols != b->rows)){
        printf("Matrices have wrong sizes!\n");
        exit(EXIT_FAILURE);
    }

    matrix *c = Init(a->rows, b->cols);


    for (int i = 0; i < a->rows; i++) {
        for (int j = 0; j < b->cols; j++) {
            int sum = 0;
            for (int k = 0; k < a->cols; k++) {
                sum += a->data[i * a->cols + k] * b->data[k * b->cols + j];
            }
            c->data[i * b->cols + j] = sum;
        }
    }

    return c;

}


void Free(matrix *m){
    free(m->data);
    free(m);
}


int main(){
    srand(time(NULL));

    //Matrix 1
    matrix *m1 = Init(2, 3);
    RandomFill(m1);
    printf("---=== M 1 ===---\n");
    Print(m1);

    //Matrix 2
    matrix *m2 = Init(3, 2);
    RandomFill(m2);
    printf("---=== M 2 ===---\n");
    Print(m2);


    /*
    //Matrix 3
    matrix *m3 = Add(m1, m2);
    printf("---=== M 3 ===---\n");
    Print(m3);
    free(m3->data);
    free(m3);
    */


    //Matrix 4
    matrix *m4 = Mult(m1, m2);
    printf("---=== M 4 ===---\n");
    Print(m4);    


    Free(m1);
    Free(m2);
    //Free(m3);
    Free(m4);

    return 0;

}
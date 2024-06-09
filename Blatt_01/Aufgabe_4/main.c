/* 
In Zusammenarbeit zwischen Daniel Heisig, Felix Scholzen & Simon Wagner
*/ 

#include <stdio.h>
#include <stdlib.h>
#include <time.h>


#define MAX_RAND_INT 999


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


matrix *Add(matrix *a, matrix *b, int *acts, double *time){

    clock_t start = clock();

    if((a->rows != b->rows) || (a->cols != b->cols)){
        printf("Matrices are not the same size!\n");
        exit(EXIT_FAILURE);
    }

    matrix *c = Init(a->rows, a->cols);

    for (int i = 0; i < a->rows; i++) {
        for (int j = 0; j < a->cols; j++) {
            c->data[i * c->cols + j] = (a->data[i * a->cols + j]) + (b->data[i * b->cols + j]);
            (*acts)++;
        }
    }

    clock_t end = clock();
    *time = ((double)(end - start)) / CLOCKS_PER_SEC * 1000;
    return c;

}


matrix *Mult(matrix *a, matrix *b, int *acts, double *time){

    clock_t start = clock();

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
                (*acts)++;
            }
            c->data[i * b->cols + j] = sum;
        }
    }

    clock_t end = clock();
    *time = ((double)(end - start)) / CLOCKS_PER_SEC * 1000;
    return c;

}


void Free(matrix *m){
    free(m->data);
    free(m);
}


void test_mult(int i){

    int acts;
    double time;

    //Matrix 1
    matrix *m1 = Init(i, i);
    RandomFill(m1);
    //Print(m1);

    //Matrix 2
    matrix *m2 = Init(i, i);
    RandomFill(m2);
    //Print(m2);

    //Mult Matrix
    matrix *m3 = Mult(m1, m2, &acts, &time);

    printf("%d; %lf\n", i, time);

    Free(m1);
    Free(m2);
    Free(m3);

}


void test_add(int i){

    int acts;
    double time;

    //Matrix 1
    matrix *m1 = Init(i, i);
    RandomFill(m1);
    //Print(m1);

    //Matrix 2
    matrix *m2 = Init(i, i);
    RandomFill(m2);
    //Print(m2);

    //Mult Matrix
    matrix *m3 = Add(m1, m2, &acts, &time);

    printf("%d; %lf\n", i, time);

    Free(m1);
    Free(m2);
    Free(m3);

}


int main(){
    srand(time(NULL));

    //test_mult(500);
    test_add(28018);

    return 0;

}



/*

Example Output for Multiplication:

Average test_mult(500) = 650
Average test_mult(1000) = 6270

We get approximatly:
f(x) = 67.38e^0.004533x


f(x) = 1000 (ms)
x = 595

f(x) = 2000 (ms)
x = 748

f(x) = 5000 (ms)
x = 950

f(x) = 10000 (ms)
x = 1103

*/


/*

Example Output for Addition:

Average test_mult(3000) = 56
Average test_mult(6000) = 225
Average test_mult(10000) = 630

We get approximatly:
f(x) = (77/12000000)x^(2) - (17/12000)x + 5/2


f(x) = 1000 (ms)
x = 12579

f(x) = 2000 (ms)
x = 17754

f(x) = 5000 (ms)
x = 28018

f(x) = 10000 (ms)
x = 39583

*/
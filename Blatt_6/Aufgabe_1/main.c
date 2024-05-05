// ###########################################################################################
// # In Zusammenarbeit zwischen Daniel Heisig, Felix Scholzen, Simon Wagner & Toni Kandziora #
// ###########################################################################################


#include <memory.h>
#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <limits.h>
#include <unistd.h>


void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}


// ##### ARRAY FUNCTIONS #######################################################################################

int randomInt(int minVal, int maxVal){
    int n = minVal + rand() % (maxVal - minVal + 1);
    return n;
}

void fillArray(int* arr, int size, int minVal, int maxVal){
    for(int i = 0; i < size; i++){
        arr[i] = minVal + rand() % (maxVal - minVal + 1);
    }
}

void printArr(int *arr, int size){
    for(int i = 0; i < size; i++){
        printf("% 3d ", arr[i]);
    }
    printf("\n");
}

void printCharArr(unsigned char *arr, int size){
    for(int i = 0; i < size; i++){
        printf("% 3d ", arr[i]);
    }
    printf("\n");
}

// ##### ARRAY FUNCTIONS #######################################################################################



// ##### COUNT SORT FUNCTIONS #######################################################################################

int* countSort(int *arr, int k, int size){
    clock_t start_time = clock(); // Start the clock for timing

    int *ret = calloc(size, sizeof(int));
    unsigned char *countArr = calloc(k, sizeof(unsigned char)); // Assume that we have max 255 values
    int operations = 0; 

    for(int i = 0; i < size; i++){
        countArr[arr[i]]++; //! first n
        operations++; 
    }

    //! we iterate over k and check, if we have a value in the array we do 3 operations.
    //! we will doe the 3 operations a max of n times, since we have at max n values in our count array stored
    // -> k + 3n operations
    int retIdx = 0;
    for(int i = 0; i < k; i++){
        while(countArr[i]){
            ret[retIdx] = i;
            countArr[i]--;
            retIdx++;
            operations += 3; // Three operations: assignment, decrement, increment of retIdx
        }
    }

    //! a total of k + 4n operations

    free(countArr);

    clock_t end_time = clock(); 
    double time_spent = (double)(end_time - start_time) / CLOCKS_PER_SEC;

    printf("%d,", operations);
    printf("%f,", time_spent);

    return ret;
}

// ##### COUNT SORT FUNCTIONS #######################################################################################



// ##### HEAP SORT FUNCTIONS #######################################################################################

void heapify(int arr[], int n, int i, int *steps) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && arr[left] > arr[largest]) {
        largest = left;
        (*steps)++;
    }
    if (right < n && arr[right] > arr[largest]) {
        largest = right;
        (*steps)++;
    }
    if (largest != i) {
        swap(&arr[i], &arr[largest]);
        (*steps)++;
        heapify(arr, n, largest, steps);
    }
}

int* heapSort(int arr[], int n) {
    clock_t start, end;
    double cpu_time_used;
    start = clock();

    int *sorted = calloc(n, sizeof(int));

    int steps = 0; 

    for (int i = 0; i < n; i++) {
        sorted[i] = arr[i];
        steps++;
    }

    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(sorted, n, i, &steps);

    for (int i = n - 1; i > 0; i--) {
        swap(&sorted[0], &sorted[i]);
        steps++;
        heapify(sorted, i, 0, &steps);
    }

    end = clock();
    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;

    printf("%d,", steps);
    printf("%f,", cpu_time_used);

    return sorted;
}

// ##### HEAP SORT FUNCTIONS #######################################################################################



// ##### MAP SORT FUNCTIONS #######################################################################################

int* mapSort(int a[], int n, double c) {
    clock_t start = clock(); 
    int steps = 0;
    
    int newn = (int)(n * c);
    if (newn == 0) newn = 1;
    int i, j = 0;
    int *bin = calloc(newn, sizeof(int));
    int *sorted = calloc(n, sizeof(int));

    if (!bin || !sorted) {
        free(bin);
        free(sorted);
        return NULL;
    }

    for (i = 0; i < newn; i++) {
        bin[i] = -1;
        steps++;
    }

    int max = INT_MIN, min = INT_MAX;
    for (i = 0; i < n; i++) {
        if (a[i] < min) min = a[i];
        if (a[i] > max) max = a[i];
        steps += 2;
    }

    double dist = max == min ? 1 : (double)(max - min) / (newn - 1);
    steps++;

    for (i = 0; i < n; i++) {
        int t = (int)((a[i] - min) / dist);
        if (t >= newn) t = newn - 1;
        steps++;

        for (int inserted = 0; !inserted; ) {
            steps++;
            if (bin[t] == -1) {
                bin[t] = a[i];
                inserted = 1;
            } else if (bin[t] != a[i]) {
                swap(&bin[t], &a[i]);
                t += (a[i] > bin[t]) ? -1 : 1;
                if (t < 0 || t >= newn) break;
            } else {
                inserted = 1;
            }
        }
    }

    for (i = 0; i < newn; i++) {
        if (bin[i] != -1) sorted[j++] = bin[i];
        steps++;
    }

    free(bin);

    clock_t end = clock(); 
    double time_spent = (double)(end - start) / CLOCKS_PER_SEC;

    printf("%d,", steps);
    printf("%f\n", time_spent);
    return sorted;
}


// ##### MAP SORT FUNCTIONS #######################################################################################




void tester(int minVal, int maxVal){

    srand(time(NULL));
    size_t size = randomInt(1000, 100000);
    int min = minVal;
    int max = maxVal;
    int* arr = malloc(size*sizeof(int));

    fillArray(arr, size, min, max);
    //printArr(arr, size);
    //printf("\n");

    printf("%ld,", size);

    countSort(arr, max, size);
    heapSort(arr, size);
    mapSort(arr, size, 100.0);

    free(arr);

}


int main(){

    printf("ListSize,countSort_Ops,countSort_Time,heapSort_Ops,heapSort_Time,mapSort_Ops,mapSort_Time\n");

    for(int i = 0; i < 1000; i++){
        sleep(1);
        tester(1000, 10000);
    }
    
}
// ###########################################################################
// # In Zusammenarbeit zwischen Daniel Heisig, Felix Scholzen & Simon Wagner #
// ###########################################################################


#include <memory.h>
#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <limits.h>


void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}


// ##### ARRAY FUNCTIONS #######################################################################################

void fillArray(int* arr, int size, int maxVal){
    for(int i = 0; i < size; i++){
        arr[i] = rand() % maxVal;
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

    int *ret = calloc(size, sizeof(int));
    unsigned char *countArr = calloc(k, sizeof(unsigned char)); // Assume that we have max 255 values

    for(int i = 0; i < size; i++){
        countArr[arr[i]]++; //! first n
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
        }
    }

    //! a total of k + 4n operations

    free(countArr);

    return ret;
}

// ##### COUNT SORT FUNCTIONS #######################################################################################



// ##### HEAP SORT FUNCTIONS #######################################################################################

void heapify(int arr[], int n, int i) {
    int largest = i;
    int left = 2*i + 1;
    int right = 2*i + 2;

    if (left < n && arr[left] > arr[largest])
        largest = left;
    if (right < n && arr[right] > arr[largest])
        largest = right;
    if (largest != i) {
        swap(&arr[i], &arr[largest]);
        heapify(arr, n, largest);
    }
}

int* heapSort(int arr[], int n) {
    int *sorted = calloc(n, sizeof(int));

    for (int i = 0; i < n; i++)
        sorted[i] = arr[i];

    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(sorted, n, i);

    for (int i = n - 1; i > 0; i--) {
        swap(&sorted[0], &sorted[i]);
        heapify(sorted, i, 0);
    }

    return sorted;
}

// ##### HEAP SORT FUNCTIONS #######################################################################################



// ##### MAP SORT FUNCTIONS #######################################################################################

int* mapSort(int a[], int n, double c) {
    if (c <= 0) {
        fprintf(stderr, "Scale factor must be positive.\n");
        return NULL;
    }

    int newn = (int)(n * c);
    int i, j = 0;
    int *bin = (int *)calloc(newn, sizeof(int));
    int *sorted = (int *)calloc(n, sizeof(int));

    if (!bin || !sorted) {
        fprintf(stderr, "Memory allocation failed.\n");
        free(bin);
        free(sorted);
        return NULL;
    }

    for (i = 0; i < newn; i++) {
        bin[i] = -1;
    }

    int max = INT_MIN, min = INT_MAX;
    for (i = 0; i < n; i++) {
        if (a[i] < min) min = a[i];
        if (a[i] > max) max = a[i];
    }

    if (min == max) { // All elements are the same
        free(bin);
        for (i = 0; i < n; i++) sorted[i] = min;
        return sorted;
    }

    double dist = (double)(max - min) / (newn - 1);

    for (i = 0; i < n; i++) {
        int t = (int)((a[i] - min) / dist);
        if (t >= newn) t = newn - 1; // Edge case for the max element
        int insert = a[i], left = 0;

        while (bin[t] != -1 && bin[t] != insert) {
            if (left) {
                if (insert > bin[t]) {
                    swap(&bin[t], &insert);
                }
                if (t > 0) t--;
                else left = 0;
            } else {
                if (insert <= bin[t]) {
                    swap(&bin[t], &insert);
                }
                if (t < newn - 1) t++;
                else left = 1;
            }
        }

        bin[t] = insert;
    }

    for (i = 0; i < newn; i++) {
        if (bin[i] != -1) sorted[j++] = bin[i];
    }

    free(bin);
    return sorted;
}

// ##### MAP SORT FUNCTIONS #######################################################################################




int main(){

    size_t size = 20;
    int k = 100;
    srand(time(NULL));
    int* arr = malloc(size*sizeof(int));

    fillArray(arr, size, k);
    printArr(arr, size);

    //int* countSortedArr = countSort(arr, k, size);
    //int* countSortedArr = heapSort(arr, size);
    int* countSortedArr = mapSort(arr, size, 30.0);
    
    printArr(countSortedArr, size);

    free(arr);
    return 0;

}
#include "memory.h"
#include "stdio.h"
#include "time.h"
#include "stdlib.h"

void fillArray(int* arr, int size, int maxVal)
{
    for(int i = 0; i < size; i++)
    {
        arr[i] = rand() % maxVal;
    }
}

void printArr(int *arr, int size)
{
    for(int i = 0; i < size; i++)
    {
        printf("% 3d ", arr[i]);
    }
    printf("\n");
}

void printCharArr(unsigned char *arr, int size)
{
    for(int i = 0; i < size; i++)
    {
        printf("% 3d ", arr[i]);
    }
    printf("\n");
}


int* countSort(int *arr, int k, int size)
{
    int *ret = calloc(size, sizeof(int));
    unsigned char *countArr = calloc(k, sizeof(unsigned char)); // Assume that we have max 255 values

    for(int i = 0; i < size; i++)
    {
        countArr[arr[i]]++; //! first n
    }


    //! we iterate over k and check, if we have a value in the array we do 3 operations.
    //! we will doe the 3 operations a max of n times, since we have at max n values in our count array stored
    // -> k + 3n operations
    int retIdx = 0;
    for(int i = 0; i < k; i++)
    {
        while(countArr[i])
        {
            ret[retIdx] = i;
            countArr[i]--;
            retIdx++;
        }
    }

    //! a total of k + 4n operations

    free(countArr);

    return ret;
}


int main()
{
    size_t size = 20;
    int k = 100;
    srand(time(NULL));
    int* arr = malloc(size*sizeof(int));

    fillArray(arr, size, k);
    printArr(arr, size);

    int* countSortedArr = countSort(arr, k, size);
    printArr(countSortedArr, size);
}
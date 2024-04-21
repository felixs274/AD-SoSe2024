#
# In Zusammenarbeit zwischen Daniel Heisig, Felix Scholzen & Simon Wagner
#
import random
import copy


# helper
def copy_array_on_call_and_print_arr(orig_func):
    def wrapper(arr):
        cloned_arr = copy.copy(arr)
        orig_func(cloned_arr)
        print(f"algo {orig_func.__name__}:", cloned_arr)
    
    return wrapper


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


# Task 1.1
@copy_array_on_call_and_print_arr
def insertion_sort(arr):
    i = len(arr)-1
    while i >= 0:
        j = i 
        while j < len(arr) - 1 and arr[j] > arr[j+1]:
            swap(arr, j, j+1)
            j = j + 1

        i = i - 1

# Task 1.2
@copy_array_on_call_and_print_arr
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-1):
            if arr[j] > arr[j+1]:
                swap(arr, j, j+1)

# Task 1.3
@copy_array_on_call_and_print_arr
def selection_sort(arr):
    for n in range(len(arr)-1, 0, -1):
        maxVal = arr[n]
        maxIdx = n
        for m in range(n-1, -1, -1):
            if arr[m] > maxVal:
                maxVal = arr[m]
                maxIdx = m
        
        swap(arr, maxIdx, n)


# Task 1.4
def quick_partition(arr, leftIdx, rightIdx):
    pivotIdx = random.randint(leftIdx, rightIdx)  # Select a random pivot index within the given range
    pivotVal = arr[pivotIdx]
    swap(arr, pivotIdx, rightIdx)  # Move pivot element to the end
    p = leftIdx
    for i in range(leftIdx, rightIdx):
        if arr[i] <= pivotVal:
            swap(arr, i, p)
            p += 1
    swap(arr, p, rightIdx)  # Move pivot element to its final sorted position
    return p

def quick_sort_rec(arr, leftIdx, rightIdx):
   if leftIdx < rightIdx:
       pivot = quick_partition(arr, leftIdx, rightIdx)
       quick_sort_rec(arr, leftIdx, pivot-1)
       quick_sort_rec(arr, pivot+1, rightIdx)

@copy_array_on_call_and_print_arr
def quick_sort(arr):
    quick_sort_rec(arr, 0, len(arr)-1)


def main():
    example_list = [20, 8, 17, 3, 14, 9, 1, 12, 5, 18, 7, 15, 2, 11, 19, 6, 10, 4, 13, 16]
    print(f"example list: {example_list}")

    insertion_sort(example_list)
    bubble_sort(example_list)
    quick_sort(example_list)
    selection_sort(example_list)


main()
#
# In Zusammenarbeit zwischen Daniel Heisig, Felix Scholzen & Simon Wagner
#

import random

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


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


def quick_sort(arr):
    quick_sort_rec(arr, 0, len(arr)-1)


def canBeCalculated(arr, aiIdx, s):
    quick_sort(arr)
    
    aj_to_find = s - arr[aiIdx]
    for ajIdx in range(len(arr)):
        if ajIdx == aiIdx:
            continue

        aj = arr[ajIdx]
        if aj == aj_to_find:
            return True

    return False


def main():
    arr = [1,2,3,4,5,7,8]

    assert canBeCalculated(arr, 0, 8) == True
    assert canBeCalculated(arr, 0, 10) == False


main()
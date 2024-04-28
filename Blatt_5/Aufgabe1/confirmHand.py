#
# In Zusammenarbeit zwischen Daniel Heisig, Felix Scholzen & Simon Wagner
#

import random
import copy

def swap(arr, i1, i2):
    arr[i1], arr[i2] = arr[i2], arr[i1]


def merge(arr1, arr2):
    i1, i2 = 0, 0
    mergedArr = []
    while i1 < len(arr1) or i2 < len(arr2):
        if i1 >= len(arr1):
            while i2 < len(arr2):
                mergedArr.append(arr2[i2])
                i2 += 1
        elif i2 >= len(arr2):
            while i1 < len(arr1):
                mergedArr.append(arr1[i1])
                i1 += 1
        else:
            if arr1[i1] < arr2[i2]:
                mergedArr.append(arr1[i1])
                i1 += 1
            else:
                mergedArr.append(arr2[i2])
                i2 += 1

    return mergedArr


def ms(arr, i1, i2):
    if len(arr) == 1:
        print(f"a[{i1}:{i2}] = {arr}")
        return arr

    i = len(arr) // 2
    a1 = ms(arr[:i], i1, i1+i-1)
    a2 = ms(arr[i:], i1+i, i2)

    newArr = merge(a1, a2)
    print(f"a[{i1}:{i2}] = {newArr}")

    return newArr

def merge_sort(arr):
    return ms(arr, 0, len(arr)-1)

def heapify(arr, idx = 0):
    iMax = len(arr) - 1
    lIdx = idx*2+1
    rIdx = idx*2+2

    if lIdx <= iMax and rIdx <= iMax:
        heapify(arr, lIdx)
        heapify(arr, rIdx)
        insertIntoHeap(arr, idx, iMax)
    elif lIdx <= iMax:
        heapify(arr, lIdx)
        insertIntoHeap(arr, idx, iMax)
    else:
        pass


def insertIntoHeap(arr, idx, iMax):
    lIdx = idx*2+1
    rIdx = idx*2+2

    if rIdx <= iMax and lIdx <= iMax:
        lSmaller = arr[idx] < arr[lIdx]
        rSmaller = arr[idx] < arr[rIdx]

        if lSmaller and rSmaller:
            if arr[lIdx] > arr[rIdx]:
                swap(arr, idx, lIdx)
                insertIntoHeap(arr, lIdx, iMax)
            else:
                swap(arr, idx, rIdx)
                insertIntoHeap(arr, lIdx, iMax)
        elif lSmaller:
            swap(arr, idx, lIdx)
            insertIntoHeap(arr, lIdx, iMax)
        elif lSmaller:
            swap(arr, idx, rIdx)
            insertIntoHeap(arr, rIdx, iMax)
        else:
            return 

    if lIdx <= iMax:
        if arr[idx] < arr[lIdx]:
            swap(arr, idx, lIdx)
            insertIntoHeap(arr, lIdx, iMax)
        else:
            return

    else:
        return


def heap_sort(arr):
    heapify(arr)

    idxBack = len(arr) - 1

    while idxBack > 0:
        print(f"{len(arr) - idxBack}: {arr}")
        swap(arr, 0, idxBack)
        idxBack -= 1
        insertIntoHeap(arr, 0, idxBack)

def main():
    origArr = [-5,13,-32,7,-3,17,23,12,-35,19]
    print(f"original array: {origArr}")
    mergeArr = merge_sort(origArr)
    print(f"merge array: {mergeArr}")

    heapArr = copy.copy(origArr)
    heap_sort(heapArr)
    print(f"heap array: {heapArr}")

    sortedArr = sorted(origArr)

    assert mergeArr == sortedArr
    assert heapArr == sortedArr


main()
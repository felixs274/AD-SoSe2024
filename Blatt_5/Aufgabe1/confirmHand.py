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


def heapify(arr, f, l, root):
    largest = root
    left = f + (root-f)*2+1
    right = f + (root-f)*2+2

    if left <= l and arr[left] > arr[root]:
        largest = left

    if right <= l and arr[right] > arr[largest]:
        largest = right

    if largest != root:
        arr[root], arr[largest] = arr[largest], arr[root]
        heapify(arr, f, l, largest)


def build_heap(arr, f, l):
    n = l - f + 1
    for i in range(f + (n - 2) // 2, f - 1, -1):
        heapify(arr, f, l, i)


def print_heap(heap):

    def get_children(idx):
        left = 2*idx + 1
        right = 2*idx + 2
        children = []
        if left < len(heap):
            children.append(heap[left])
        if right < len(heap):
            children.append(heap[right])
        return children

    def calculate_height(heap_size):
        height = 0
        while 2 ** height - 1 < heap_size:
            height += 1
        return height

    def print_level(level, height):
        indent = " " * ((2 ** (height-1)-1)*3)
        space = " " * ((2 ** height)-1)
        print(indent, end="")
        print(space.join([str(item).center(6) for item in level]))

    level = [heap[0]]
    heap_size = len(heap)
    height = calculate_height(heap_size)
    index = 0

    while level:
        print_level(level, height)

        next_level = []
        for item in level:
            next_level.extend(get_children(index))
            index += 1

        level = next_level
        height -= 1


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
    build_heap(arr, 0, len(arr)-1)
    print_heap(arr)

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
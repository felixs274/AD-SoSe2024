import random
import copy

def swap(arr, i1, i2):
    arr[i1], arr[i2] = arr[i2], arr[i1]


def insertion_sort(arr, n):
    if n == 1:
        return
    
    insertion_sort(arr, n-1)

    lastElemToSort = arr[n-1]

    j = n-2

    while j >= 0 and arr[j] > lastElemToSort:
        swap(arr, j, j+1)
        j -= 1


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

class Node:
    def __init__(self, arr, parentNode):
        self.arr = arr
        self.leftNode = None
        self.rightNode = None
        self.parentNode = parentNode
    
    def split(self):
        if len(self.arr) > 1:
            i = len(self.arr) // 2
            self.leftNode = Node(self.arr[:i], self)
            self.rightNode = Node(self.arr[i:], self)

    def hasNoChildren(self):
        return (self.leftNode is None) and (self.rightNode is None)

    def hasChildren(self):
        return not self.hasNoChildren()

    def getChildren(self):
        return [self.leftNode, self.rightNode]

    def mergeChildren(self):
        self.arr = merge(self.leftNode.arr, self.rightNode.arr)
        self.leftNode = None
        self.rightNode = None


class MergeTree:
    def __init__(self, arr):
        self._motherOfAllNodes = Node(arr, None)
    
    def splitTreeIntoNodes(self):
        nodesToWorkOn = [self._motherOfAllNodes]
        while nodesToWorkOn:
            n = nodesToWorkOn.pop()
            n.split()
            if n.hasChildren():
                nodesToWorkOn.extend(n.getChildren())

    def mergeNodesIntoOne(self):
        currentNode = self._motherOfAllNodes
        while currentNode is not None:
            if currentNode.hasNoChildren():
                currentNode = currentNode.parentNode
            elif currentNode.leftNode.hasNoChildren() and \
                currentNode.rightNode.hasNoChildren():
                # print(f"mergeing: {currentNode.leftNode.arr}, {currentNode.rightNode.arr} = ", end="")
                currentNode.mergeChildren()
                # print(currentNode.arr)
            else:
                if currentNode.leftNode.hasChildren():
                    currentNode = currentNode.leftNode
                else:
                    currentNode = currentNode.rightNode

    def getResult(self):
        return self._motherOfAllNodes.arr


def merge_sort(arr):
    algo = MergeTree(arr)
    algo.splitTreeIntoNodes()
    algo.mergeNodesIntoOne()
    resArr = algo.getResult()
    for i in range(len(arr)):
        arr[i] = resArr[i]



def main():
    origArr = [random.randint(0, 20) for _ in range(10)]
    insArr = copy.copy(origArr)
    mergeArr = copy.copy(origArr)
    print(f"original array: {origArr}")
    insertion_sort(insArr, len(insArr))
    print(f"insertion array: {insArr}")
    merge_sort(mergeArr)
    print(f"merge array: {mergeArr}")

    sortedArr = sorted(origArr)

    assert insArr == sortedArr
    assert mergeArr == sortedArr


main()
#
# in Zusammenarbeit mit Simon Wagner, Felix Scholzen und Daniel Heisig entstanden
#

import random

class Node:
    prevNode = None
    nextNode = None
    value = None

    def __init__(self, val, prevNode=None, nextNode=None):
        self.prevNode = prevNode
        self.nextNode = nextNode
        self.value = val

   
    def __len__(self):
        i = 1
        n = self
        while n.nextNode:
            i += 1
            n = n.nextNode
        
        return i
    
    def lastNode(self):
        n = self
        while n.nextNode:
            n = n.nextNode
        
        return n


def partition(start, end):
    pivot = end
    pivot_val = pivot.value
    current = start
    while start != end:
        if start.value < pivot_val:
            start.value, current.value = current.value, start.value
            current = current.nextNode
        start = start.nextNode
    current.value, pivot.value = pivot.value, current.value
    return current

def quicksort(start, end):
    if start == end or not start or not end or start == end.nextNode:
        return
    pivot_prev = partition(start, end)
    quicksort(start, pivot_prev.prevNode)
    quicksort(pivot_prev.nextNode, end)

def arrToLinkedList(arr):

    firstNode = Node(arr[0])
    secondNode = Node(arr[1], firstNode)
    firstNode.nextNode = secondNode
    prevNode = firstNode
    currentNode = secondNode
    for i in range(2, len(arr)):
        prevNode = currentNode
        currentNode = Node(arr[i])

        prevNode.nextNode = currentNode
        currentNode.prevNode = prevNode
    
    return firstNode


def printList(linkedList):
    n = linkedList

    print(n.value, end=" ")

    while n := n.nextNode:
        print(n.value, end = " ")
    
    print()

def main():

    arr = [1,2,3,4,5,6,7,8,9]

    random.shuffle(arr)
    linkedList = arrToLinkedList(arr)
    printList(linkedList)
    quicksort(linkedList, linkedList.lastNode())
    printList(linkedList)

main()
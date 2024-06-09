#
# In Zusammenarbeit mit Simon Wagner, Toni Kandziora, Daniel Heisig, Felix Scholzen entstanden
#

import random

class PriorityElement:
    def __init__(self, key, value):
        self.key, self.value = key, value

class PriorityQueue:
    def __init__(self):
        self._queue = list()

    # has complexity O(n) since loop over every element
    def getWholeQueue(self):
        return [e.value for e in self._queue]

    # we want to insert element e at the specified pos
    # so we move every element += 1
    # therefore has complexity O(n) since we have to loop over whole array
    def _insertIntoQueue(self, element, pos):
        
        self._queue.append(None)
        i = len(self._queue) - 1
        while i > pos:
            self._queue[i] = self._queue[i - 1]
            i -= 1
        
        self._queue[pos] = element

    # has complexity of O(n) since we loop first over the array until we find where to insert. Then we move the rest of the array on position further 
    def insert(self, key, value):
        toInsert = PriorityElement(key, value)

        if len(self._queue) == 0:
            self._queue.append(toInsert)
            return

        for i, e in enumerate(self._queue):
            if e.key < toInsert.key:
                self._insertIntoQueue(toInsert, i)
                return
        
        self._queue.append(toInsert)
    

    # Complexity of O(n) since we move every element one down starting from the position.
    def remove(self, pos):
        # since pos is the position in the queue, and we are reverse, we need to change the index ...
        startIdx = len(self._queue) - pos - 1
        endIdx = len(self._queue) - 1
        for i in range(startIdx, endIdx):
            self._queue[i] = self._queue[i+1]
        
        self._queue.pop()

    # O(1) since we just access the array at its last position
    def getMin(self):
        return self._queue[-1].value if len(self._queue) else None

    # O(1) sincd we just access the array and remove the last element
    def extractMin(self):
        return self._queue.pop().value if len(self._queue) else None

    # O(n) since we only loop 2 times over the array
    def decreaseKey(self, elem, pos, key):
        self.remove(pos)
        self.insert(key, elem)
        

def checkBasicQueue():
    queue = PriorityQueue()
    listToTest = random.choices([*range(10)], k=10)
    for e in listToTest:
        queue.insert(e, e)
        print(e, [e.value for e in queue._queue])
    
    sortedList = []
    while (e := queue.extractMin()) is not None:
        sortedList.append(e)

    print(f"list: {listToTest}")
    print(f"sorted: {sorted(listToTest)}")
    print(f"queue: {sortedList}")


    assert sorted(listToTest) == sortedList


def checkPosDecrease():
    queue = PriorityQueue()

    for e in range(5):
        queue.insert(e, e)

    wq = queue.getWholeQueue()
    assert wq  == [4, 3, 2, 1, 0]

    queue.decreaseKey(4, 4, 0)

    wq = queue.getWholeQueue()
    assert wq == [3, 2, 1, 0, 4]

    queue.decreaseKey(3, 4, 1)

    wq = queue.getWholeQueue()
    assert wq == [2, 1, 3, 0, 4]


def main():
    checkBasicQueue()
    checkPosDecrease()

main()
#
# In Zusammenarbeit mit Simon Wagner, Toni Kandziora, Daniel Heisig, Felix Scholzen entstanden
#

import math

class BasicHashtable:
    def __init__(self, m):
        self._m = m
        self._field = [None for _ in range(m)]
    
    def insert(self, key):
        pass

    def print(self):
        print(f"{self.__class__.__name__}:")
        for idx, key in enumerate(self._field):
            print(f"    {idx}: {key}")
    
    def h(self, s):
        x = (math.sqrt(5) - 1) / 2
        return int(self._m * ((s*x) % 1))


class LinearHashtable(BasicHashtable):
    def insert(self, key):
        idx = self.h(key)

        tries = 0
        while self._field[(idx + tries) % self._m] is not None:
            if tries == self._m: # hash table is full
                raise IndexError("hash table is full")
            tries += 1

        self._field[idx+tries] = key


class QuadraticHashtable(BasicHashtable):
    def insert(self, key):
        hval = self.h(key)
        
        i = 0
        mappedIdx = hval
        idxval = self._field[mappedIdx]
        while idxval is not None:
            i += 1
            mappedIdx = (hval + (1 * i) + (3 * i ** 2)) % self._m
            idxval = self._field[mappedIdx]

        self._field[mappedIdx] = key


class DoubleHashtable(BasicHashtable):
    def h1(self, s):
        return s

    def h2(self, s):
        return 1 + s % (self._m - 1)

        
    def insert(self, key):

        i = 0
        hidx = self.h1(key) % self._m
        hval = self._field[hidx]
        while hval is not None:
            i += 1
            hidx = (self.h1(key) + i*self.h2(key)) % self._m
            hval = self._field[hidx]
        
        self._field[hidx] = key


def main():
    listToHash = [10, 22, 31, 4, 15, 28, 17, 88, 59]
    lh = LinearHashtable(11)
    qh = QuadraticHashtable(11)
    dh = DoubleHashtable(11)

    for val in listToHash:
        lh.insert(val)
        qh.insert(val)
        dh.insert(val)
    
    lh.print()
    qh.print()
    dh.print()


main()
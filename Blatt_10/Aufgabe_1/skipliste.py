import random


def coinflip():
    return random.random() > 0.5


class Node:
    def __init__(self, value):
        self.value = value
        self.refsToNextVal = []

    def height(self):
        return len(self.refsToNextVal)

    def updateRef(self, layer, node):
        if len(self.refsToNextVal) <= layer:
            self.refsToNextVal.append(node)
        else:
            self.refsToNextVal[layer] = node

    def delTopRef(self):
        self.refsToNextVal.pop()

    def hasRefAtLayer(self, layer):
        return self.height() > layer

    def getRefAtLayer(self, layer):
        return self.refsToNextVal[layer]

    def __repr__(self) -> str:
        return f"Node({self.value})"

    def __str__(self) -> str:
        return self.__repr__()


class SkipListe:
    # Initialisiert eine leere Skip-Liste
    def __init__(self):
        self._firstLayer = []

    def deinit(self):
        self.init()

    # Gibt die aktuelle Skip-Liste aus (z.B. auf der Konsole)
    def printList(self):
        if len(self._firstLayer) == 0:
            return

        strlist = ["" for _ in range(len(self._firstLayer))]

        totalHeight = len(self._firstLayer)

        refs = [{e.value} for e in self._firstLayer]

        n = self._firstLayer[0]
        while n:
            for layer in range(totalHeight):
                s = f" {n.value:^4} "

                if layer < n.height():
                    refs[layer].add(n.refsToNextVal[layer].value)

                if n.value in refs[layer]:
                    strlist[layer] += s
                else:
                    strlist[layer] += "-" * len(s)

            n = n.refsToNextVal[0] if len(n.refsToNextVal) else None

        retstr = ""
        for s in strlist[-1::-1]:
            retstr += s + "\n"

        print(retstr, end="")

    # Fügt einen Schlüssel k in die Skip-Liste ein
    def insert(self, k):
        if self.search(k):
            # print(f"val {k} already in list")
            return

        toInsert = Node(k)

        if len(self._firstLayer) == 0:
            self._firstLayer.append(toInsert)
            return

        layer = 0
        while True:
            if layer >= len(self._firstLayer):
                self._firstLayer.append(toInsert)
                break

            lastNode = self._firstLayer[layer]

            if toInsert.value < lastNode.value:
                self._firstLayer[layer] = toInsert
                toInsert.updateRef(layer, lastNode)
                return

            while True:
                node = lastNode.refsToNextVal[layer] if layer < lastNode.height(
                ) else None

                if node:
                    if node.value < toInsert.value:
                        lastNode = node
                    else:
                        lastNode.updateRef(layer, toInsert)
                        toInsert.updateRef(layer, node)
                        break

                else:
                    lastNode.updateRef(layer, toInsert)
                    break

            if coinflip() == True:
                layer += 1
            else:
                break

    # Entfernt einen Schl¨ussel k aus der Skip-Liste

    def delete(self, k):
        firstLayerLen = len(self._firstLayer)
        for layer in range(firstLayerLen):
            layer = firstLayerLen - layer - 1
            node = self._firstLayer[layer]

            if node.value == k:
                if node.hasRefAtLayer(layer):
                    self._firstLayer[layer] = node.getRefAtLayer(layer)
                else:
                    self._firstLayer.pop()

            while node.hasRefAtLayer(layer):
                nn = node.getRefAtLayer(layer)
                if nn.value == k:

                    if nn.hasRefAtLayer(layer):
                        ref = nn.getRefAtLayer(layer)
                        node.updateRef(layer, ref)
                    else:
                        node.delTopRef()

                    break
                elif nn.value > k:
                    break

                node = nn

    # Gibt true zurück, wenn der Schlüssel k in der Skip-Liste vorhanden ist sonst nichts

    def search(self, k):
        layer = len(self._firstLayer)-1
        if layer == -1:
            return False

        refList = self._firstLayer

        while layer >= 0:
            if layer >= len(refList):
                layer -= 1
                continue

            if refList[layer].value < k:
                refList = refList[layer].refsToNextVal
            elif refList[layer].value > k:
                layer -= 1
            else:
                return True

        return False


randlist = None
n = 0


def gn(listlen=7, nrange=100):
    global randlist
    global n
    if randlist is None:
        if True:
            randlist = [int(random.random() * nrange) for _ in range(listlen)]
        else:
            randlist = [2, 17, 18, 21, 24, 26, 32, 40, 44,
                        49, 56, 61, 67, 75, 78, 79, 82, 83, 89, 1]

    e = randlist[n]
    n = (n + 1) % len(randlist)
    return e


def main():
    sl = SkipListe()

    numbers = 10000

    for i in range(numbers):
        number = gn(numbers, numbers)
        sl.insert(number)

        if i % 1000 == 0:
            print(f"inserting: {number}")
            print(f"{round(i / numbers * 100, 2)}%")
            # sl.printList()
            print("*"*20)

    for i in range(numbers):
        number = gn(numbers, numbers)
        sl.delete(number)

        if i % 1000 == 0:
            print(f"deleting: {number}")
            print(f"{round(i / numbers * 100, 2)}%")

            # sl.printList()
            print("*"*20)


main()

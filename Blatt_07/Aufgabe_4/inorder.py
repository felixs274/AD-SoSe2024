# In Zusammenarbeit mit Simon Wagner, Toni Kandziora, Felix Scholzen, Daniel Heisig entstanden

class AVLNode:
    classCount = 0
    def __init__(self, leftNode=None, rightNode=None):
        self.val = None
        self.leftNode = leftNode
        self.rightNode = rightNode

    def toStr(self, top=True):
        if top:
            AVLNode.classCount = 0

        ret = "("
        if self.leftNode:
            ret += self.leftNode.toStr(False)
        
        ret += ","
        if self.val is None:
            AVLNode.classCount += 1
            self.val = AVLNode.classCount
        ret += str(self.val)
        ret += ","

        if self.rightNode:
            ret += self.rightNode.toStr(False)
        
        ret += ")"
        
        return ret


def constructMinimalTree(height=5):
    if height == 1:
        return [AVLNode()]
    elif height == 2:
        node1 = AVLNode()
        node1.leftNode = AVLNode()

        node2 = AVLNode()
        node2.rightNode = AVLNode()
        return [node1, node2]

    mintrees1 = constructMinimalTree(height-1)
    mintrees2 = constructMinimalTree(height-2)

    retTrees = []

    for mintree1 in mintrees1:
        for mintree2 in mintrees2:
            retTrees.append(AVLNode(mintree1, mintree2))
            retTrees.append(AVLNode(mintree2, mintree1))


    return retTrees


def main():
    mintrees = constructMinimalTree(5)
    for t in mintrees:
        print(t.toStr())

    print(f"there are {len(mintrees)} minimal avl trees")

main()
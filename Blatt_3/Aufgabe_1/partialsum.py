import sys

# tanken from https://svn.blender.org/svnroot/bf-blender/trunk/blender/build_files/scons/tools/bcolors.py
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def printCombination(inp, x1, y1, x2, y2):

    for y in range(len(inp)):
        for x in range(len(inp[0])):
            color = ""
            if x1 <= x <= x2 and y1 <= y <= y2:
                color = bcolors.OKGREEN
            
            print(f"|{color}{inp[y][x]:^5}{bcolors.ENDC}", end="")
        print("|")


# tanken from lecture
def getBiggestSum(row):
    s = 0
    aktSum = 0
    maxSum = -sys.maxsize

    maxX1 = 0
    maxX2 = 0

    currentX1 = 0
    currentX2 = 0
    for i, elem in enumerate(row):
        # add new element to local sum
        s = aktSum + elem
        
        # check if local sum is larger with new sum than element
        if s > elem:
            # current sum does not get negated with new element => we include it in sum
            currentX2 = i
            aktSum = s
        else:
            # it is better to not include element in sum, we reset local sum
            currentX1 = i
            currentX2 = i
            aktSum = elem
        
        # check if local sum is larger than the global sum, if yes print it out 
        if aktSum > maxSum:
            maxX1 = currentX1
            maxX2 = currentX2
            maxSum = aktSum
    
    return maxX1, maxX2, maxSum


def solvePartialSum(inp):
    xSize, ySize = len(inp[0]), len(inp)

    maxX1, maxX2, maxY1, maxY2 = 0,0,0,0
    maxSum = 0

    # iterate over all possible possible partial Y sizes
    for yWindowSize in range(1, ySize+1):
        #iterate over all possible y offsets
        for yOffset in range(0, (ySize+1)-yWindowSize):
            partialAdded = [0 for _ in range(xSize)]
            # add y row in partial y window
            for y in range(yWindowSize):
                y = y + yOffset
                for x in range(xSize):
                    partialAdded[x] += inp[y][x]
            
            # search for biggest parital sum in y window
            x1, x2, biggestRowSum = getBiggestSum(partialAdded)
            if biggestRowSum > maxSum:
                maxX1, maxX2 = x1, x2
                maxY1 = yOffset
                maxY2 = yOffset + yWindowSize - 1
                maxSum = biggestRowSum

    return (maxX1, maxY1), (maxX2, maxY2), maxSum


def main():
    inp5by5 = [
        [1,-2,3-4,5],
        [3,-5,-5,-1,5],
        [-5,2,1,3,1],
        [5,6,1,-5,9],
        [3,3,4,5,1]
    ]

    exerciseInp = [
        [-3, 7, -17],
        [8, -1, 12],
        [2, -3, 4]
    ]

    inp = exerciseInp

    biggestSum = solvePartialSum(inp)

    print(f"point1: {[*biggestSum[0]]} point2: {[*biggestSum[1]]} sum: {biggestSum[2]}")
    printCombination(inp, *biggestSum[0], *biggestSum[1])


main()
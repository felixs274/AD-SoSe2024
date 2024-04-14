

def recursiveImpl(n, m):
    if n == 0:
        return m + 1
    elif m == 0 and n >= 1:
        return recursiveImpl(n-1, 1)
    else:
        return recursiveImpl(n-1, recursiveImpl(n, m-1))


def iterativeImpl(n, m):
    resultStackN = []
    resultStackM = []
    resultStack = []
    while action := opstack.pop():
        match action:
            case "normal_op":
                if n == 0:
                    result = m + 1
                elif m == 0 and n >= 1:
                    opstack.push("normal_op")

# in Zusammenarbeit mit Simon Wagner, Felix Scholzen, Daniel Heisig entstanden

def recursiveImpl(n, m):
    if n == 0:
        return m + 1
    elif m == 0 and n >= 1:
        return recursiveImpl(n-1, 1)
    else:
        return recursiveImpl(n-1, recursiveImpl(n, m-1))


def iterativeImpl(m, n):
    stack = [m]
    while stack:
        m = stack.pop()
        if m == 0:
            n = n + 1
        elif n == 0:
            n = 1
            stack.append(m-1)
        else:
            n = n - 1
            stack.extend([m-1, m])

    return n


def main():
    for n in range(2, 10):
        for m in range(2, 10):

            #rec = recursiveImpl(n, m)
            it = iterativeImpl(n, m)
            #print(f"{n=},{m=}: {rec:<3} {it:<3}")
            print(f"{n=},{m=}: {it:<3}")
# max output:
"""
n=2,m=2: 7  
n=2,m=3: 9  
n=2,m=4: 11 
n=2,m=5: 13 
n=2,m=6: 15 
n=2,m=7: 17 
n=2,m=8: 19 
n=2,m=9: 21 
n=3,m=2: 29 
n=3,m=3: 61 
n=3,m=4: 125
n=3,m=5: 253
n=3,m=6: 509
n=3,m=7: 1021
n=3,m=8: 2045
n=3,m=9: 4093
"""

main()

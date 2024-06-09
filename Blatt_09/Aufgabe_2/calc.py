#
# In Zusammenarbeit mit Simon Wagner, Toni Kandziora, Daniel Heisig, Felix Scholzen entstanden
#

import math

def h(s):
    x = (math.sqrt(5) - 1) / 2
    m = 1000
    return int(m * ((s*x) % 1))

def main():
    numbers = [61, 62, 63, 64, 65]

    for n in numbers:
        key = h(n)
        print(f"{n}: {key}")


# Result:
# 61: 700
# 62: 318
# 63: 936
# 64: 554
# 65: 172
main()

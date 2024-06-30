#
# In Zusammenarbeit mit Simon Wagner, Toni Kandziora, Daniel Heisig, Felix Scholzen entstanden
#

import sys


class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m


def calcRuntime(matrices):
    n = len(matrices)
    if n == 0:
        return 0

    # dimensions of the matrices in chain order
    p = [matrices[0].n] + [matrices[i].m for i in range(n)]

    # minimum multiplication costs
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # splitting points
    s = [[0 for _ in range(n)] for _ in range(n)]

    # L is chain length
    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            dp[i][j] = sys.maxsize
            for k in range(i, j):
                q = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < dp[i][j]:
                    dp[i][j] = q
                    s[i][j] = k

    return dp[0][n - 1]


def main():
    matrices = [
        Matrix(30, 35),
        Matrix(35, 15),
        Matrix(15, 5),
        Matrix(5, 10),
        Matrix(10, 20),
        Matrix(20, 25)
    ]
    m = calcRuntime(matrices)

    print(f"minimal number of multiplications are: {m}")


main()

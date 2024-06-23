def floyd_warshall(n, edges):
    # Unendliche Distanz initialisieren
    inf = float('inf')

    # Distanz- und Vorgängermatrix initialisieren
    D = [[inf] * n for _ in range(n)]
    pi = [[None] * n for _ in range(n)]

    # Selbstschleifen mit 0 initialisieren
    for i in range(n):
        D[i][i] = 0
        pi[i][i] = i

    # Kanten initialisieren
    for u, v, w in edges:
        D[u-1][v-1] = w
        pi[u-1][v-1] = u

    # Floyd-Warshall-Algorithmus ausführen
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][j] > D[i][k] + D[k][j]:
                    D[i][j] = D[i][k] + D[k][j]
                    pi[i][j] = pi[k][j]

    return D, pi


def main():
    # Knotenanzahl
    n = 4

    # Kanten: (Startknoten, Endknoten, Gewicht)
    edges = [
        (1, 2, 1),
        (2, 3, 1),
        (3, 4, 1),
        (1, 4, 5)
    ]

    D, pi = floyd_warshall(n, edges)

    print("Distanzmatrix D:")
    for row in D:
        print(row)

    print("\nVorgängermatrix π:")
    for row in pi:
        print(row)


main()

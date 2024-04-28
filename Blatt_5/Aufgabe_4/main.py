import time





# Variante 1
def variante1(M, N):

    O11 = M[0][0] * N[0][0] + M[0][1] * N[1][0]
    O12 = M[0][0] * N[0][1] + M[0][1] * N[1][1]
    O21 = M[1][0] * N[0][0] + M[1][1] * N[1][0]
    O22 = M[1][0] * N[0][1] + M[1][1] * N[1][1]

    return [[O11, O12], [O21, O22]]



# Variante 2
def variante2(M, N):

    H1 = (M[0][0] + M[1][1]) * (N[0][0] + N[1][1])
    H2 = (M[1][0] + M[1][1]) * N[0][0]
    H3 = M[0][0] * (N[0][1] - N[1][1])
    H4 = M[1][1] * (N[1][0] - N[0][0])
    H5 = (M[0][0] + M[0][1]) * N[1][1]
    H6 = (M[1][0] - M[0][0]) * (N[0][0] + N[0][1])
    H7 = (M[0][1] - M[1][1]) * (N[1][0] + N[1][1])

    O11 = H1 + H4 - H5 + H7
    O12 = H3 + H5
    O21 = H2 + H4
    O22 = H1 - H2 + H3 + H6

    return [[O11, O12], [O21, O22]]




def matrix_multiply(a,b):

    start_time = time.time()

    c = []
    for i in range(0,len(a)):
        temp=[]
        for j in range(0,len(b[0])):
            s = 0
            for k in range(0,len(a[0])):
                s += a[i][k]*b[k][j]
            temp.append(s)
        c.append(temp)

    # Pint Time
    end_time = time.time()
    duration = end_time - start_time
    print(duration)

    return c





def main():

    # Matrix M & N

    M = [[1, 2], [3, 4]]

    N = [[5, 6], [7, 8]]



    #print(variante1(M, N))
    #print(variante2(M, N))

    print(matrix_multiply(M, N))
    print(strassen(M, N))
   


main()
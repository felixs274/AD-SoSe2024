#
# In Zusammenarbeit zwischen Daniel Heisig, Felix Scholzen & Simon Wagner
#



import time, random



# Variante 1
def variante1(M, N):

    start_time = time.time()

    O11 = M[0][0] * N[0][0] + M[0][1] * N[1][0]
    O12 = M[0][0] * N[0][1] + M[0][1] * N[1][1]
    O21 = M[1][0] * N[0][0] + M[1][1] * N[1][0]
    O22 = M[1][0] * N[0][1] + M[1][1] * N[1][1]

    # Print Time
    end_time = time.time()
    duration = end_time - start_time
    print(duration)

    return [[O11, O12], [O21, O22]]



# Variante 2
def variante2(M, N):

    start_time = time.time()

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

    # Print Time
    end_time = time.time()
    duration = end_time - start_time
    print(duration)

    return [[O11, O12], [O21, O22]]



def matrix_multiply(a,b):

    c = []
    for i in range(0,len(a)):
        temp=[]
        for j in range(0,len(b[0])):
            s = 0
            for k in range(0,len(a[0])):
                s += a[i][k]*b[k][j]
            temp.append(s)
        c.append(temp)

    return c



# STRASSEN ALGORITHM -------------------------------------------------------------------

def matrix_add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def matrix_subtract(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def strassen_matrix_multiplication(A, B):
    if len(A) == 1:
        return [[A[0][0] * B[0][0]]]
    else:
        # Dividing the matrices into quadrants
        mid = len(A) // 2

        A11 = [row[:mid] for row in A[:mid]]
        A12 = [row[mid:] for row in A[:mid]]
        A21 = [row[:mid] for row in A[mid:]]
        A22 = [row[mid:] for row in A[mid:]]

        B11 = [row[:mid] for row in B[:mid]]
        B12 = [row[mid:] for row in B[:mid]]
        B21 = [row[:mid] for row in B[mid:]]
        B22 = [row[mid:] for row in B[mid:]]

        # Calculating p1 to p7:
        p1 = strassen_matrix_multiplication(matrix_add(A11, A22), matrix_add(B11, B22))
        p2 = strassen_matrix_multiplication(matrix_add(A21, A22), B11)
        p3 = strassen_matrix_multiplication(A11, matrix_subtract(B12, B22))
        p4 = strassen_matrix_multiplication(A22, matrix_subtract(B21, B11))
        p5 = strassen_matrix_multiplication(matrix_add(A11, A12), B22)
        p6 = strassen_matrix_multiplication(matrix_subtract(A21, A11), matrix_add(B11, B12))
        p7 = strassen_matrix_multiplication(matrix_subtract(A12, A22), matrix_add(B21, B22))

        # Re-combining the four parts of the result matrix
        C11 = matrix_add(matrix_subtract(matrix_add(p1, p4), p5), p7)
        C12 = matrix_add(p3, p5)
        C21 = matrix_add(p2, p4)
        C22 = matrix_add(matrix_subtract(matrix_add(p1, p3), p2), p6)

        # Constructing the whole matrix from halves
        top = [C11[i] + C12[i] for i in range(len(C11))]
        bottom = [C21[i] + C22[i] for i in range(len(C21))]
        return top + bottom

# ------------------------------------------------------------------------------------------------------


def timer(fun, a, b):
    start_time = time.time()
    res = fun(a, b)
    end_time = time.time()
    duration = end_time - start_time
    print(duration)   
    return res


def main():

    # Matrix M & N

    M = [[1, 2], [3, 4]]

    N = [[5, 6], [7, 8]]

    #print(variante1(M, N))
    #print(variante2(M, N))
    
  
    # For Strassen ---------------------------------------------------------------------------------------

    A = [[random.randint(1, 100) for _ in range(100)] for _ in range(100)]
    B = [[random.randint(1, 100) for _ in range(100)] for _ in range(100)]

    #print(timer(strassen_matrix_multiplication, A, B))
    timer(matrix_multiply, A, B)

main()
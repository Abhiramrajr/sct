import numpy as np

def max_min(R,S):
    result = np.zeros((R.shape[0],S.shape[1]))
    for i in range(R.shape[0]):
        for j in range(S.shape[1]):
            minmax = 0
            for k in range(R.shape[1]):
                minmax = max(minmax,min(R[i,k],S[k,j]))
            result[i,j] = minmax
    return result

m = int(input("Enter the no.of rows of 1st : "))
n = int(input("Enter the no.of columns 1st : "))

p = int(input("Enter the no.of rows 2nd : "))
q = int(input("Enter the no.of columns 2nd : "))

if n != p:
    print("Cant perform operation !!!")
else:
    print("Enter the elements of 1st matrix")
    elements1 = []
    for i in range(m):
        for j in range(n):
            elements1.append(float(input()))
    
    print("Enter the element of 2nd matrix ")
    elements2 = []
    for x in range(p):
        for z in range(q):
            elements2.append(float(input()))

    matrix1 = np.array(elements1).reshape(m,n)
    matrix2 = np.array(elements2).reshape(p,q)
    
    print(matrix1)
    print(matrix2)
    
    matrix3 = max_min(matrix1,matrix2)
    print(matrix3)
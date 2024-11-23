def complement(C):
    d = C.copy()
    for i,j in d.items():
        d[i] = round(1 - j,2)
    return d

def union(A,B):
    d = A.copy()
    for i,j in B.items():
        d[i] = max(d[i],j)
    return d

def intersection(A,B):
    d = A.copy()
    for i,j in B.items():
        d[i] = min(d[i],j)
    return d

A = {}
B = {}

n = int(input("Enter the no of items : "))

for i in range(n):
    key = input("Enter key: ")  # Key as a string
    value = float(input(f"Enter value for {key}: "))  # Value as a float
    A[key] = value
    value = float(input(f"Enter value for {key}: "))
    B[key] = value
    
print("Set 1 :",A)
print("Set 2 :",B)

LHS = complement(union(A, B))
RHS = intersection(complement(A), complement(B))

if LHS == RHS:
    print("De Morgans verified")
    
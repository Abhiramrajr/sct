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

def complement(C):
    d = C.copy()
    for i,j in d.items():
        d[i] = round(1 - j,2)
    return d

A = {}
B = {}
# Get the number of key-value pairs to input
n = int(input("Enter the number of elements: "))

# Taking input for each key-value pair
for _ in range(n):
    key = input("Enter key: ")  # Key as a string
    value = float(input(f"Enter value for {key}: "))  # Value as a float
    A[key] = value
    value = float(input(f"Enter value for {key}: "))
    B[key] = value
print("Set 1 :",A)
print("Set 2 :",B)

result = union(A,B)
inter = intersection(A,B)
comp = complement(A)
compB = complement(B)

print("A U B = ",result)
print("A intersection B",inter)
print("A' = ",comp)
print("B' = ",compB)
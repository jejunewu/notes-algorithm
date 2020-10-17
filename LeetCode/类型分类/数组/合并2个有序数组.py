A = []
B = [1]

m,n = len(A), len(B)

############################
A += [0]*n

p, p1, p2 = m+n-1,m-1,n-1

while p1 >= 0 and p2 >= 0:

    if A[p1] > B[p2]:
        A[p] = A[p1]
        p1-=1
    else:
        A[p] = B[p2]
        p2-=1
    p-=1


if p1 == -1:
    A[0:p+1] = B[0:p+1]
if p2 == -1:
    A[0:p+1] = A[0:p+1]

print(A)
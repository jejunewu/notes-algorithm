def validMountainArray(A) -> bool:

    i, size = 0, len(A)
    up,down = 0, 0

    while i<size-1 and A[i] < A[i+1]:
        up+=1
        i+=1
    while i<size-1 and A[i] > A[i+1]:
        down+=1
        i+=1

    return up+1+down == size and up>0 and down>0



################### Test ########################
A = [0,3,2,1]
res = validMountainArray(A)
print(res)
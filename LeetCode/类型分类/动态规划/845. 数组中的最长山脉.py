
def longestMountain(A):
    size = len(A)
    up = [1] * size
    down = [1] * size

    for i in range(1, size):
        if A[i] > A[i-1]:
            up[i] = up[i-1]+1

        if A[size - i -1] > A[size-i]:
            down[size-i-1] = down[size-i]+1

    res = 0
    for i in range(1, size-1):
        if A[i-1] < A[i] and A[i] > A[i+1]:
            res = max(res, up[i] + down[i] - 1)

    return res

################### Test ########################
A = [2,1,4,7,3,2,5]
ans = longestMountain(A)
print(ans)
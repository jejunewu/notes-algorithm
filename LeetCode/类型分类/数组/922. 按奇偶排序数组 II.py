def sortArrayByParityII(A):
    odd = []
    even = []
    for i in A:
        if i&1 ==1:
            odd.append(i)
        else:
            even.append(i)
    for j in range(len(A)>>1):
        print(j)
        A[2*j]=odd[j]
        A[2*j+1] = even[j]
    return A

################### Test ########################
A = [2,5]
ans = sortArrayByParityII(A)

print(ans)
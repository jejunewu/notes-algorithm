def hammingWeight(n: int) -> int:

    ans = 0
    while n > 0:
        if n&1 == 1:
            ans+=1
        n >>= 1

    return ans


################### Test ########################
ans = hammingWeight(5)
print(ans)
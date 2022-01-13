def isPowerOfTwo(n: int) -> bool:
    return n>0 and n&(n-1) == 0

t = isPowerOfTwo(1)
print(t)
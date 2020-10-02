
def hammingWeight(n: int) -> int:
    ans=0
    mask = 1
    for i in range(32):
        if n & mask != 0:
            ans+=1

        mask<<=1
    return ans
s='00000000000000000000000000001011'
t = hammingWeight(int(s))
print(t)
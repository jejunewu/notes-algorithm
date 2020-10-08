def sumNums(n: int) -> int:
    return n and n + sumNums(n-1)

t = sumNums(9)
print(t)

# def t():
#     return 5 and 6
#
# s = t()
# print(s)
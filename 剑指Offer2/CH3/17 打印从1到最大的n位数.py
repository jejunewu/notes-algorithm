def printNumbers(n: int):
    res = []
    for i in range(1, int(n*'9')+1):
        res.append(i)
    return res


################### Test ########################
ans = printNumbers(2)

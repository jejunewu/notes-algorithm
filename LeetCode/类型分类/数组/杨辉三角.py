def triangle(n):

    res = []
    for i in range(n+1):
        res.append([1])
        j = 1
        while j < i:
            if j == i-1:
                res[i].append(1)
                break
            res[i].append(res[i-1][j-1] +res[i-1][j])
            j+=1
    return res[1:]
n = 0
ans = triangle(n)
print(ans)
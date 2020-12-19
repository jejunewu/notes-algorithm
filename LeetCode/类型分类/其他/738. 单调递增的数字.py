def monotoneIncreasingDigits(N: int):
    arr = list(str(N))
    res = []
    i = len(arr)-1

    while i-1 >= 0:
        if arr[i] >= arr[i-1]:
            res.append(arr[i])
        else:
            arr[i-1] = str(int(arr[i-1])-1)
            res = ['9']*(len(res)+1)
        i-=1

    if arr[i]!='0':
        res.append(arr[i])

    return ''.join(res)[::-1]


N = 1234
ans = monotoneIncreasingDigits(N)
print(ans)
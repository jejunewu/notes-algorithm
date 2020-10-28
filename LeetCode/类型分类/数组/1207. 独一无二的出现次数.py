def uniqueOccurrences(arr):

    tmp = [[],[]]

    for e in arr:
        if e in tmp[0]:
            tmp[1][tmp[0].index(e)] += 1
        else:
            tmp[0].append(e)
            tmp[1].append(1)

    return sorted(tmp[1]) == sorted(list(set(tmp[1])))


################### Test ########################
arr = [1,2,2,1,1,3,3]
ans = uniqueOccurrences(arr)
print(ans)
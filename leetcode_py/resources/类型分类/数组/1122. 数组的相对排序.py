def relativeSortArray(arr1, arr2):

    start = 0
    for i in arr2:
        for j in range(start, len(arr1)):
            if arr1[j] == i:
                arr1[start], arr1[j] = arr1[j], arr1[start]
                start+=1
            # print(j)
        # print(i)
    # arr1 = arr1[:start] + sorted(arr1[start+1:])
    return arr1[:start] + sorted(arr1[start+1:])


################### Test ########################
# arr1 = [28,6,22,8,44,17]
# arr2 = [22,28,8,6]

arr1 = [33,22,48,4,39,36,41,47,15,45]
arr2 = [22,33,48,4]

ans = relativeSortArray(arr1, arr2)
print(ans)
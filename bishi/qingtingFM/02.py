arr = sorted([1,2,3,4,5])

def findTarget(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

ans = findTarget(arr, 7)
print(ans)
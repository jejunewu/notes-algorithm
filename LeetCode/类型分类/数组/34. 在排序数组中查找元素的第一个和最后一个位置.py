def searchRange(nums, target):
    L,R = -1,-1

    for i in range(len(nums)):
        if (i==0  or  (i>0 and nums[i-1]<target)) and nums[i] == target :
            L = i

        if (i == len(nums)-1 or (i < len(nums)-1 and nums[i + 1] > target)) and nums[i] == target:
            R = i
            # print(nums[i])
    return L, R



nums = [2]
target = 2

ans = searchRange(nums, target)
print(ans)
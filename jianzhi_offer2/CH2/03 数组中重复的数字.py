def findRepeatNumber(nums):

    nums = sorted(nums)
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return nums[i]

################### Test ########################

nums = [2, 3, 1, 0, 2, 5, 3]
ans = findRepeatNumber(nums)
print(ans)
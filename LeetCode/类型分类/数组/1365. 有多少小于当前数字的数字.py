def smallerNumbersThanCurrent(nums):

    sortNums = sorted(nums)

    for i in range(len(nums)):
        nums[i] = sortNums.index(nums[i])
    return nums

################### Test ########################
nums = [7,7,7,7]
ans = smallerNumbersThanCurrent(nums)
print(ans)

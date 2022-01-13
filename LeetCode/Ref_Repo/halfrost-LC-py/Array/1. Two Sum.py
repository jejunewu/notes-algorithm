def twoSum(nums, target):
    lens = len(nums)
    for i in range(lens - 1):
        for j in range(i+1, lens):
            if nums[i]+nums[j] == target:
                return [i,j]

# 解法2
'''
字典法
'''
def twoSum2(nums, target):
    lens = len(nums)
    dict = {}
    for i in range(lens):
        another = target - nums[i]
        # print(dict)
        if another in dict:
            return [dict[another], i]
        dict[nums[i]] = i
        # print(i)

nums = [2, 7, 11, 15]
target = 13

###
ans = twoSum2(nums, target)
print(ans)

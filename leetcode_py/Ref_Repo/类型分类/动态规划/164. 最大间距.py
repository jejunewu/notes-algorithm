def maximumGap(nums):
    lens = len(nums)
    if lens < 2:
        return 0
    nums = sorted(nums)
    dp, i = [0] * lens, 0
    while i + 1 < lens:
        dp[i + 1] = nums[i + 1] - nums[i]
        i += 1
    return max(dp)


nums = [10,11]
ans = maximumGap(nums)
print(ans)
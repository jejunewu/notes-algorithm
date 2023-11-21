def permute(nums):
    n = len(nums)
    res = []

    def dfs(first=0):
        if first == n:
            res.append(nums[:])
        for i in range(first, n):
            nums[i], nums[first] = nums[first], nums[i]
            dfs(first + 1)
            nums[first], nums[i] = nums[i], nums[first]

    dfs()

    return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    res = permute(nums)
    print(res)

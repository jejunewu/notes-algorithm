import itertools as it
def subsets(nums):
    ans = []
    n=0
    while n <= len(nums):
        for i in it.combinations(nums,n):
            ans.append(list(i))
        n+=1
    return ans

def subsets2(nums):
    def dfs(nums, k, c, res):
        if k >= len(nums):
            res.append(c.copy())
            return
        c.append(nums[k])
        dfs(nums, k + 1, c, res)
        c.pop()
        dfs(nums, k + 1, c, res)

    res=[]
    dfs(nums, 0, [], res)
    return res


nums = [1, 2, 3]
ans = subsets2(nums)
print(ans)
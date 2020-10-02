nums = [4,1,2,1,2,1,2]

ans = 0

for num in nums:
    ans^=num

print(ans)

t = int((sum(set(nums))*3 - sum(nums))/2)

print(t)
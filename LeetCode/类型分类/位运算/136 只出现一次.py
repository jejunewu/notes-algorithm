nums = [4,1,2,1,2]

print(nums)

ans = 0

for num in nums:
    ans^=num

print(ans)

#######################

ans2 = int(sum(set(nums))*2 - sum(nums))
print(ans2)
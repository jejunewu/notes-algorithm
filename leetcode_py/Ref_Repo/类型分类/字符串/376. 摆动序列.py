def wiggleMaxLength(nums):

    tmp = []
    for i in range(1, len(nums)):
        tmp.append(nums[i] - nums[i-1])

    print(tmp)
    pre = tmp[0]
    ans = 2
    for i in range(1,len(tmp)):
        if tmp[i]*pre < 0:
            print(tmp[i])
            ans+=1
            pre = tmp[i]
    print(11111111111111)
    return ans

def wiggleMaxLength2(nums):
    if len(nums) == 0:
        return 0
    stack = []
    for i in range(1, len(nums)):
        if nums[i] - nums[i-1] > 0:
            if len(stack) == 0 or stack[-1] == -1:
                stack.append(1)
            else:
                nums[i] = nums[i-1]

        elif nums[i] - nums[i-1] < 0:
            if len(stack) == 0 or stack[-1] == 1:
                stack.append(-1)
            else:
                nums[i] = nums[i-1]
    print(nums)
    return 1 if len(set(nums)) == 1 else len(stack)+1

def wiggleMaxLength3(nums):
    if len(nums) <= 1:
        return len(nums)
    up, down = 1, 1
    for i in range(1, len(nums)):
        if nums[i] - nums[i - 1] > 0:
            up = down + 1
        elif nums[i] - nums[i - 1] < 0:
            down = up + 1
    return max(up, down)



nums = [33,53,12,64,50,41,45,21,97,35,47,92,39,0,93,55,40,46,69,42,6,95,51,68,72,9,32,84,34,64,6,2,26,98,3,43,30,60,3,68,82,9,97,19,27,98,99,4,30,96,37,9,78,43,64,4,65,30,84,90,87,64,18,50,60,1,40,32,48,50,76,100,57,29,63,53,46,57,93,98,42,80,82,9,41,55,69,84,82,79,30,79,18,97,67,23,52,38,74,15]
ans = wiggleMaxLength3(nums)
print(ans)
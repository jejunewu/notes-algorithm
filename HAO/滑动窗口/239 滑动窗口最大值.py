def maxSlidingWindow(nums, k):

    return nums

nums = [1,3,-1,-3,5,3,6,7]
k = 3

### 暴力法 ###
'''
res = []
for i in range(len(nums)-k+1):
    res.append(max(nums[i:i+k]))
    print(i)
print(res)
'''

### 双端队列法 ###
queue = []
res = []

for i in range(len(nums)):

    #删除当前元素小的值
    while i>0 and len(queue)>0 and nums[i] > queue[-1]:
        queue = queue[: len(queue)-1]

    queue.append(nums[i])

    #维护队列
    if i>=k and nums[i-k] == queue[0]:
        queue = queue[1:]

    #添加到res
    if i>=k-1:
        res.append(queue[0])

    print(queue)
print(res)

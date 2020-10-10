import numpy as np
# t = np.random.randint(1,10,10)

t = list(range(1,32))[::-1]
lens = len(t)
print(t)
#####选择排序
nums = 0
for i in range(0,lens-1):
    minIdx = i
    for j in range(i+1, lens):
        if t[j] < t[minIdx]:
            minIdx = j
    nums+=1
    t[i],t[minIdx] = t[minIdx],t[i]


print(t)
print(nums)
import numpy as np
t = np.random.randint(1,10,10)
lens = len(t)
print(t)
#####选择排序

for i in range(0,lens-1):
    minIdx = i
    for j in range(i+1, lens):
        if t[j] < t[minIdx]:
            minIdx = j

    t[i],t[minIdx] = t[minIdx],t[i]


print(t)
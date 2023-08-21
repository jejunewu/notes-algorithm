import numpy as np
t = np.random.randint(1,10,10)

print(t)
#####冒泡排序
lens = len(t)

for i in range(0, lens-1):
    for j in range(i+1, lens):
        if t[i] > t[j]:
            t[i],t[j] = t[j],t[i]


print(t)